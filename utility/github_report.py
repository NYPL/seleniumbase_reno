"""
pytest plugin: GitHub Actions report of each test's FINAL outcome (port of the
github-final.ts Playwright reporter in dxp-react-search).

With --reruns, a test that fails and then passes on a retry is "flaky", not a failure:
  - ::error   for tests that failed after all reruns
  - ::warning for flaky tests (failed at least once, then passed)
  - nothing   for tests that passed first try
It also writes a Passed / Flaky / Failed / Skipped table to GITHUB_STEP_SUMMARY.
Only active when running in GitHub Actions (GITHUB_ACTIONS=true).
"""
import os

# nodeid -> {"reruns": int, "failed": bool, "skipped": bool, "location": tuple, "message": str}
_results = {}


def _entry(report):
    return _results.setdefault(report.nodeid, {
        "reruns": 0, "failed": False, "skipped": False,
        "location": report.location, "message": "",
    })


def _first_line(report):
    crash = getattr(report.longrepr, "reprcrash", None)
    text = crash.message if crash else str(report.longrepr or "")
    return text.strip().splitlines()[0] if text.strip() else "unknown error"


def pytest_runtest_logreport(report):
    entry = _entry(report)
    if report.outcome == "rerun":  # failed attempt that pytest-rerunfailures will retry
        entry["reruns"] += 1
        entry["message"] = _first_line(report)
    elif report.failed:
        entry["failed"] = True
        entry["message"] = _first_line(report)
    elif report.skipped and report.when == "setup":
        entry["skipped"] = True


def _escape_data(value):
    return value.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")


def _escape_property(value):
    return _escape_data(value).replace(":", "%3A").replace(",", "%2C")


def _annotate(level, nodeid, entry, message):
    path, line, _ = entry["location"]
    props = f"file={_escape_property(path)},line={(line or 0) + 1},title={_escape_property(nodeid)}"
    print(f"::{level} {props}::{_escape_data(nodeid + ': ' + message)}")


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    # with pytest-xdist (-n), only the main process reports; workers only see their own tests
    if hasattr(config, "workerinput") or os.getenv("GITHUB_ACTIONS") != "true" or not _results:
        return

    failed = [n for n, e in _results.items() if e["failed"]]
    flaky = [n for n, e in _results.items() if not e["failed"] and not e["skipped"] and e["reruns"]]
    skipped = [n for n, e in _results.items() if e["skipped"]]
    passed = len(_results) - len(failed) - len(flaky) - len(skipped)

    for nodeid in flaky:
        entry = _results[nodeid]
        _annotate("warning", nodeid, entry,
                  f"Flaky: passed on attempt {entry['reruns'] + 1} after {entry['reruns']} failed attempt(s). "
                  f"Last failure: {entry['message']}")
    for nodeid in failed:
        entry = _results[nodeid]
        _annotate("error", nodeid, entry, f"Failed after {entry['reruns'] + 1} attempt(s): {entry['message']}")

    summary_file = os.getenv("GITHUB_STEP_SUMMARY")
    if not summary_file:
        return
    lines = [
        f"## pytest: {'✅ passed' if not failed else '❌ failed'}", "",
        "| Passed | Flaky | Failed | Skipped |", "|---|---|---|---|",
        f"| {passed} | {len(flaky)} | {len(failed)} | {len(skipped)} |",
    ]
    if failed:
        lines += ["", "### ❌ Failed", ""] + [f"- {n}" for n in failed]
    if flaky:
        lines += ["", "### ⚠️ Flaky (failed, then passed on retry)", "",
                  "These did not fail the run but may point at slow or unstable pages.", ""]
        lines += [f"- {n}" for n in flaky]
    with open(summary_file, "a") as f:
        f.write("\n".join(lines) + "\n")
