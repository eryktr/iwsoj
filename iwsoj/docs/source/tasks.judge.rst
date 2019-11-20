tasks.judge package
===================

Submodules
----------

tasks.judge.errors module
-------------------------
| `error.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/tasks/judge/errors.py>`_
|
| The function **__init__** from the class **IncorrectSolutionError** is used to inform a user which public test was failed. 
|
| If public test fails, the user will see **INCORRECT_SOLUTION**. The is the information about user's output for the tested task's input and expected output.
|
| If the test is implicit, the user will not see that information in case of test would fail.

.. automodule:: tasks.judge.errors
   :members:
   :undoc-members:
   :show-inheritance:

tasks.judge.judge module
------------------------
| `judge.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/tasks/judge/judge.py>`_
|
| The funcion named **judge** is intended to check the correctness of the solution of the task.
| The sourcecode is tested as follows:

- program checks if the user's sourcecode was compiled correctly for the input from table named **tasks_task** from the database
- program compare results return by dockerfile with the results expected by data from row output from table named **tasks_task** from the database
- if all results in output are equal, the **judge** returns true, otherwise false


.. automodule:: tasks.judge.judge
   :members:
   :undoc-members:
   :show-inheritance:


Module contents
---------------

.. automodule:: tasks.judge
   :members:
   :undoc-members:
   :show-inheritance:
