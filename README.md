# iwsoj
Intelligent Web-Based Scalable Online Judge

# Workflow
1. **master** is a protected branch - pushing directly to it blocked.
2. In order to apply changes to master, you need to create a side-branch and then open a **pull request** against master.
3. You need to get at least one **approval** to be able to **merge** the pull request.
4. If there are **unresolved comments** about your pull request, do not merge it until all comments have been resolved.
5. For the ease of documentation generation, please use **docstrings** in the language of your choice.
6. If you know how to improve a certain area of a pull request, please, come up with a helpful **snippet**.
7. Code should be tested. **Unit tests**, maybe mocked, are enough to start with, but we will want to introduce integration testing later on.

# Installation
1. Clone the repository
2. Move into the topmost **iwsoj** dir
3. Make sure that **python3.7** is installed
4. Create a new virtual environment for encapsulation purposes
  
            python3 -m venv env

5. Activate the newly generated environment:

            source env/bin/activate
            
6. Install the necessary dependencies:
            
             pip3 install -r requirements.txt
             
7. Define a new running configuration as 

            python3 iwsoj/manage.py runserver
            
 # Project structure
 
iwsoj/
├── db.sqlite3 - dummy datbase, will be replaced later on
├── iwsoj
├── ├── static - all static files (frontend) go here
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py - routing file
│   ├── views.py - http responses for api
│   └── wsgi.py
├── manage.py
└── tests - all python tests go here
    ├── conftest.py - we put global-scope test fixtures into this file
    └── __init__.py

