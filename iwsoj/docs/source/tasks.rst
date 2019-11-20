tasks package
=============

Subpackages
-----------

.. toctree::

   tasks.judge
   tasks.migrations
   tasks.serializers

Submodules
----------

tasks.admin module
------------------
| `admin.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/tasks/admin.py>`_

.. automodule:: tasks.admin
   :members:
   :undoc-members:
   :show-inheritance:

tasks.api module
----------------
| `api.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/tasks/api.py>`_
|
| The file **api.py** and class **TaskViewSet** are intended to provide access to users to available tasks from database which are stored in the table named **tasks_task** . The tasks are stored in the **queryset** after successfull authentication.
|
| The class protects access to tasks againts unauthenticated users. 
|
| The access is authenticated by AuthUserToken which is set in field **authentication_classes**. If program got uncorrect or non-existent token, the program would denied access to tasks.
| We have the access thanks path: **api/tasks/** and method Bearer. Scheme of use method Bearer:
|
| "authorization: Bearer <AuthUserToken>"
|
| Now it’s time to say something about **permission_classes**.
|
| Permission is a functionality of system what determines which request will be granted or denied. We use **permissions.IsAuthenticated** and that permission class will allow to access only for logged in user. If you are interested more about permissions and permission classes, `let's see <https://www.django-rest-framework.org/api-guide/permissions/>`_ .

.. automodule:: tasks.api
   :members:
   :undoc-members:
   :show-inheritance:

tasks.apps module
-----------------
| `apps.pu source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/tasks/apps.py>`_

.. automodule:: tasks.apps
   :members:
   :undoc-members:
   :show-inheritance:

tasks.complexity module
-----------------------
| `complexity.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/tasks/complexity.py>`_
|
| Users usually want to know about the level of difficulty of the tasks and flirt only tasks of the similar level of difficulty.
| There are a lot of tasks in the database of the different level of difficulty, from easy (1) to competitive (4).
| The author of the task has to classify the exercise before he adds its to the table **tasks_task** .
|
| The method named **toString** will help user to select all exercises with selected level of difficulty.

.. automodule:: tasks.complexity
   :members:
   :undoc-members:
   :show-inheritance:

tasks.models module
-------------------
| `models.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/tasks/models.py>`_
|
| That class imports model of the task from the table **tasks_task** from the database **db.sqlite3**.
|
| The model has **id** field and 6 important fields:

- **title** : the name of title of the task
- **statement** : the content of the task with example input and output
- **createdate** : the date of create the task
- **complexity** : the level of the difficulty of the task
- **input** : example input test parameters for the task
- **output** : output results of the task for the parameters in input field

| There are also some restriction for the fields:

- default **id** field is auto-increment
- all of fields must be **not-null**
- **title** field must have unique name, no longer than 255 characters
- **complexity** field must be an integer between 1 and 4
- default **createdate** is a date of input task to the database

| Now it's time to say something about a few methods:

- **get_complexity_display** - the method shows level of difficulty of the task
- **get_next_by_createdate** - the method shows the earliest task which was added to database after the task which is currently presented
- **get_previous_by_createdate** - the method shows the latest task which was added to database before the task which is currently presented

.. automodule:: tasks.models
   :members:
   :undoc-members:
   :show-inheritance:

tasks.urls module
-----------------
| `urls.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/tasks/urls.py>`_

.. automodule:: tasks.urls
   :members:
   :undoc-members:
   :show-inheritance:

tasks.views module
------------------
| `views.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/tasks/views.py>`_

.. automodule:: tasks.views
   :members:
   :undoc-members:
   :show-inheritance:


Module contents
---------------

.. automodule:: tasks
   :members:
   :undoc-members:
   :show-inheritance:
