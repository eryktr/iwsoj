tasks.serializers package
=========================

Submodules
----------

tasks.serializers.task\_serializer module
-----------------------------------------
| `task_serializer source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/tasks/serializers/task_serializer.py>`_
|
| The function named **create** from class named TaskSerializer is used to create a new task and add it to the database.

| The method requires  fields:

- **title** : the name of title of the task, TEXT type
- **statement** : the content of the task with example input and output, TEXT type
- **complexity** : the level of the difficulty of the task, INT type
- **input** : example input test parameters for the task, TEXT type
- **output** : output results of the task for the parameters in input field, TEXT type

| There are also some restriction for the fields:

- default **id** field is auto-increment
- all of fields must be **not-null**
- **title** field must have unique name, no longer than 255 characters
- **complexity** field must be an integer between 1 and 4

If the method return correct object, it is added to the database.

.. automodule:: tasks.serializers.task_serializer
   :members:
   :undoc-members:
   :show-inheritance:


Module contents
---------------

.. automodule:: tasks.serializers
   :members:
   :undoc-members:
   :show-inheritance:
