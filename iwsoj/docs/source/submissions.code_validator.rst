submissions.code\_validator package
===================================

Submodules
----------

submissions.code\_validator.code\_validator module
--------------------------------------------------
| `code_validator source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/submissions/code_validator/code_validator.py>`_
|
| Function **create_tmp_file** is a function what is intended to create a temporary file to write an user source code or file with input parameters.
|
| Function **validate_code** is a method to compile code and check if result is correct.
| See below how the function works:

- selecting programming language
- getting sourcecode from the user and input file
- using `soSorryYouLose <../html/runner.html#runner.runner.soSorryYouLose>`_ file to get output
- using `judge <../html/tasks.judge.html#module-tasks.judge>`_ to compare output with the expected output of the task from the database

.. automodule:: submissions.code_validator.code_validator
   :members:
   :undoc-members:
   :show-inheritance:


Module contents
---------------

.. automodule:: submissions.code_validator
   :members:
   :undoc-members:
   :show-inheritance:
