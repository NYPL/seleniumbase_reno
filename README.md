# Purpose

This is the repo for Python/SeleniumBase testing of nypl.org. The goal of this repo is converting smoke/regression tests from manual to automated.

# Setup

Download Pycharm CE and create a new project and clone this repo.

Go to terminal in PyCharm, and run command “pip3 install seleniumbase”. Sbase must be at least 4.11.3. To upgrade, use “pip3 install seleniumbase --upgrade” 

Type “sbase” or “seleniumbase” to check if it is installed. You should see its version and other related stuff.

Install chromedriver with “sbase install chromedriver latest”.

Install requirements/dependencies with “pip freeze > requirements.txt” for Github/Jenkins integration.

Base interpreter is Python 3.10 for this test suite.

# Running Tests
 ## By Command Line
 
 cd into the nypl_tests files under examples (examples/nypl_tests) file and type 'pytest file_name'
 
 for instance: - cd ~/examples/nypl_tests 
               - pytest test_sign_up.py
               
 try adding --demo for a slower run:
 pytest test_sign_up.py --demo

               
 ## In PyCharm CE
 
 Click on the Green arrow next to the 'test_' files or right click anywhere and choose 'Run'.
 
 # Note
 
 To test the mobile tests in 'test_mobile.py', the test should be run with --mobile command on terminal, for instance:
 pytest test_mobile.py --headless --mobile



# Page Object Modeling has been used for the following pages:

header:           - https://www.nypl.org/
footer:           - https://www.nypl.org/



blog:             - https://www.nypl.org/blog
blog/all:         - https://www.nypl.org/blog/all

booklists:        - https://www.nypl.org/books-more/recommendations/125/adults
                  - https://www.nypl.org/books-more/recommendations/best-books/adults
                  - https://www.nypl.org/books-more/recommendations/staff-picks/adults
           
campaigns:        - https://www.nypl.org/125
                  - https://www.nypl.org/125/timeline
                  - https://www.nypl.org/125/topcheckouts
           
exhibitions:      - https://www.nypl.org/events/exhibitions
                  - https://www.nypl.org/events/exhibitions/upcoming
                  - https://www.nypl.org/events/exhibitions/past
                  - https://www.nypl.org/events/exhibitions/archived-exhibition-resources
                  - https://www.nypl.org/events/exhibitions/community-showcases
                  - https://www.nypl.org/events/exhibitions/online
                  - https://www.nypl.org/events/exhibitions/stonewall50
             
locations:        - https://www.nypl.org/locations

online resources: - https://www.nypl.org/research/collections/articles-databases




