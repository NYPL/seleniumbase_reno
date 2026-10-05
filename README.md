# Purpose

This is the repo for Python/SeleniumBase testing of nypl.org. The goal of this repo is converting smoke/regression tests from manual to automated.

# Setup

Download Pycharm CE and create a new project and clone this repo.

Install requirements/dependencies with “pip install -r requirements.txt”. This installs SeleniumBase (4.43.2 or newer) and pytest. SeleniumBase downloads a matching chromedriver on its own.

Type “sbase” or “seleniumbase” to check if it is installed. You should see its version and other related stuff.

Base interpreter is Python 3.11 for this test suite (same as CI).

Tests that log in read credentials from a .env file in the repo root (not committed):

 - CATALOG_USERNAME
 - CATALOG_PASSWORD
 - LCA_PASSWORD

# Repo Layout

 - tests/ : test files (test_*.py) and test data (tests/resources)
 - pages/ : page objects with locators, one file per page
 - utility/ : shared helpers (NyplUtils), base class for all tests
 - .github/workflows/ : CI workflows (smoke, regression, QA)

# Running Tests
 ## By Command Line
 
 From the repo root, run pytest against the tests folder or a single file
 
 for instance: - pytest tests/test_locations.py --headless
               - pytest tests -m smoke --headless
               - pytest tests --env=qa (runs against qa-www.nypl.org)
               
 try adding --demo for a slower run:
 pytest tests/test_locations.py --demo

               
 ## In PyCharm CE
 
 Click on the Green arrow next to the 'test_' files or right click anywhere and choose 'Run'.
 
 ## Github Actions CI/CD
 
 Click on the "Actions" tab at the top of the repository.
 
 Select the workflow you want to run from the list of workflows on the left.
 
 Click the "Run workflow" button on the right.

 Prod Smoke also runs every day at 11:00 UTC and posts failures to Slack.
