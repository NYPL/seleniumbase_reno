# Purpose

This is the repo for Python/SeleniumBase testing of nypl.org. The goal of this repo is converting smoke/regression tests from manual to automated.

# Setup

Download Pycharm CE and create a new project and clone this repo.

Go to terminal in PyCharm, and run command “pip3 install seleniumbase”. Sbase must be at least 4.11.3. To upgrade, use “pip3 install seleniumbase --upgrade” 

Type “sbase” or “seleniumbase” to check if it is installed. You should see its version and other related stuff.

Install chromedriver with “sbase install chromedriver latest”.

Install requirements/dependencies with “pip install -r requirements.txt”.

Base interpreter is Python 3.11 for this test suite (same as CI).

# Repo Layout

 - tests/ : test files (test_*.py) and test data (tests/resources)
 - pages/ : page objects with locators, one file per page
 - utility/ : shared helpers (NyplUtils), base class for all tests
 - .github/workflows/ : CI workflows (smoke, regression, QA)

# Running Tests
 ## By Command Line
 
 From the repo root, run pytest against the tests folder or a single file
 
 for instance: - pytest tests/test_sign_up.py --headless
               - pytest tests -m smoke --headless
               
 try adding --demo for a slower run:
 pytest test_sign_up.py --demo

               
 ## In PyCharm CE
 
 Click on the Green arrow next to the 'test_' files or right click anywhere and choose 'Run'.
 
 ## Github Actions CI/CD
 
 Click on the "Actions" tab at the top of the repository.
 
 Select the workflow you want to run from the list of workflows on the left.
 
 Click the "Run workflow" button on the right.
 
 # Note
 
 To test the mobile tests in 'test_mobile.py', the test should be run with --mobile command on terminal, for instance:
 pytest test_mobile.py --headless --mobile




