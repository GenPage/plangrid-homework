# plangrid-homework
Homework problem for plangrid DevOps/SRE position. I am using Flask for 
the HTTP endpoint as it is a lightweight "micro" web framework perfect
for this task.

## Files
* app.py -- The main flask app with the routes and business logic
* test_app.py -- pytests for app.py
* Dockerfile -- dockerfile for running the app
* Test-Dockerfile -- dockerfile for running tests on this app

# Running the application
Please make sure to have Docker installed on the machine. I have included
a makefile to make running commands and cmdline options easier

    make run
    
To enable the app in debug mode and get the debug logs you can use:

    make run-debug

# Testing
Testing also uses a docker container. To run it:

    make test