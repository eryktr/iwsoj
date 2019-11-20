iwsoj package
=============

Submodules
----------

iwsoj.settings module
---------------------
| `settings.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/iwsoj/settings.py>`_
|
| In this file we set settings in our program. One of the most important is **BASE_DIRED**. It is a path to that file.

| In that file we can find other settings of out program like:
- **SECRET_KEY**
- **INSTALLED_APPS** 
- **REST_FRAMEWORK**
- **MIDDLEWARE**
- **ROOT_URLCONF**
- **TEMPLATES**
- **WSGI_APPLICATION**
- **DATABASES**
- **AUTH_PASSWORD_VALIDATORS**
- **LANGUAGE_CODE**
- **TIME_ZONE**.

| **SECRET_KEY** -- that is a parametr to encrypt and decrypt important informatation. Do not share it with third parties!
|
| **INSTALLED_APPS** -- that is a list of names of all applications that are enabled in this installation
|
| **REST_FRAMEWORK** -- that is a toolkit for building Web APIs, currently we use only **rest_framework.authentication.TokenAuthentication**
|
| **MIDDLEWARE** -- that is a low-level system for globally alerting Django's input or output (request/response processing)
|
| **TEMPLATES** -- that is a text file what is intended to generate any text format like CSV, XML or HTML
|
| **WSGI_APPLICATION** -- that is a specification what is intend to describe how a web server communicates with web applications
|
| **DATABASES** -- that is an organized collection of information
|
| **AUTH_PASSWORD_VALIDATORS** -- these are specifications to authentication by the password
|
| **TIME_ZONE** -- like the name sounds, in that place we have to set our time zone, e.g. UTC for Poland and Central Europe


| If we want to add or change somenting in our program, we have to check, if all of required settings are set here.
| Otherwise our program in compile time raises a lot of errors.

.. automodule:: iwsoj.settings
   :members:
   :undoc-members:
   :show-inheritance:

iwsoj.urls module
-----------------
| `urls.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/iwsoj/urls.py>`_
|
| In this file we can find paths that allow: 

- request urls which create static webstites
- registration
- login
- access to task
- access to submissions.

Additionally, to registration is required: 

- username
- firstname
- email
- password.

Additionally, to login is required: 

- username
- password.

Additionally, to get access to task or submissons, authorization token of logged in user is required.

.. automodule:: iwsoj.urls
   :members:
   :undoc-members:
   :show-inheritance:

iwsoj.views module
------------------
| `views.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/iwsoj/views.py>`_
|
| Class urls.py methods to call static webstites collaborate with methods from this file. Currently we have only one function named home. Lets open the port 8000 is open and define a new configuration: 
|
| python3 iwsoj/manage.py runserver 
|
| We will get response **Nothing to find here. Use the /api tree.** and HTTP status 404.

.. automodule:: iwsoj.views
   :members:
   :undoc-members:
   :show-inheritance:

iwsoj.wsgi module
-----------------
| `wsgi.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/iwsoj/wsgi.py>`_
|
.. automodule:: iwsoj.wsgi
   :members:
   :undoc-members:
   :show-inheritance:


Module contents
---------------

.. automodule:: iwsoj
   :members:
   :undoc-members:
   :show-inheritance:
