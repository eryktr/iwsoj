submissions package
===================

Subpackages
-----------

.. toctree::

   submissions.code_validator
   submissions.migrations
   submissions.serializers

Submodules
----------

submissions.admin module
------------------------

| `admin.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/submissions/admin.py>`_

.. automodule:: submissions.admin
   :members:
   :undoc-members:
   :show-inheritance:

submissions.api module
----------------------
| `api.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/submissions/api.py>`_
|
| The file **api.py** and class **SubmissionViewSet** are intended to provide access to users to available tasks from database which are stored in the table named **submissions_submission** . The submissions are stored in the **queryset** after successfull authentication.
|
| The class protects access to submissions againts unauthenticated users. 
|
| The access is authenticated by AuthUserToken which is set in field **authentication_classes**. If program got uncorrect or non-existent token, the program would denied access to submissions.
| We have the access thanks path: **api/submissions/** and method Bearer. Scheme of use method Bearer:
|
| "authorization: Bearer <AuthUserToken>"
|
| Now it’s time to say something about **permission_classes**.
|
| Permission is a functionality of system what determines which request will be granted or denied. We use **permissions.IsAuthenticated** and that permission class will allow to access only for logged in user. If you are interested more about permissions and permission classes, `let's see <https://www.django-rest-framework.org/api-guide/permissions/>`_ .

.. automodule:: submissions.api
   :members:
   :undoc-members:
   :show-inheritance:

submissions.apps module
-----------------------
| `app.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/submissions/apps.py>`

.. automodule:: submissions.apps
   :members:
   :undoc-members:
   :show-inheritance:

submissions.language module
---------------------------
| `language.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/submissions/language.py>`_
|
| The class Language is intended to select the language of the submissions.
|
| Function **get_suffix** is a method to indentify the programming language by the suffix of the name.

.. automodule:: submissions.language
   :members:
   :undoc-members:
   :show-inheritance:

submissions.models module
-------------------------
| `models.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/submissions/models.py>`_
|
| That class imports model of the task from the table **tasks_task** from the database **db.sqlite3**.
|
| The model has **id** field and 6 important fields:

- **user** : id number of `user <../html/users.html>`_
- **task** : id number of `task <../html/tasks.html>`_ 
- **status** : `status <../html/submissions.html#submissions-status-module>`_ of the solutnion of the task
- **sourceCode** : the code which was written by a user 
- **language** : `programming language <../html/submissions.html#submissions-language-module>`_ of the task
- **createdate** : the date of create the sumbission
- **error** : the error which caused during the compilation or running the program

| There are also some restriction for the fields:

- default **id** field is auto-increment
- all of fields expect **error** must be **not-null**
- default **createdate** is a date of input task to the database

| Now it's time to say something about a few methods:

- **get_language_display** - the method shows `the language <../html/submissions.html#submissions-language-module>`_ of the submission
- **get_next_by_createdate** - the method shows the earliest submission which was added to database after the sumbission which is currently presented
- **get_previous_by_createdate** - the method shows the latest submission which was added to database before the submission which is currently presented
- **get_status_display** - the method shows `the status <../html/submissions.html#submissions-status-module>`_ of the submission 

.. automodule:: submissions.models
   :members:
   :undoc-members:
   :show-inheritance:

submissions.status module
-------------------------
| `status.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/submissions/status.py>`_
|
| The class Status return the result of the tasks. There are 7 basic results of the task:

- **Passed** : code was correctly compiled and all of the tests are passed
- **Wrong answer** : code was correctly compiled, but not all of the test are passed
- **Memory limit exceeded** : OutOfMemoryError error occurred
- **Runtime error** : the program is carried out indefinitely
- **Time limit exceeded** : TimeoutError error occurred
- **Compilation error** : CompilationError error occurred
- **Internal system error** : other error occurred

| If you want to read more about the errors, click `here <../html/runner.html#runner-error-module>`_

.. automodule:: submissions.status
   :members:
   :undoc-members:
   :show-inheritance:

submissions.urls module
-----------------------
| `urls.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/submissions/urls.py>`_

.. automodule:: submissions.urls
   :members:
   :undoc-members:
   :show-inheritance:

submissions.views module
------------------------
| `views source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/submissions/views.py>`_

.. automodule:: submissions.views
   :members:
   :undoc-members:
   :show-inheritance:


Module contents
---------------

.. automodule:: submissions
   :members:
   :undoc-members:
   :show-inheritance:
