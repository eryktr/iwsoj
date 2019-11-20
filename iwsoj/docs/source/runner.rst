runner package
==============

Submodules
----------

runner.error module
-------------------
| `error.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/runner/error.py>`_
|
| Even the best programmers commit errors and make mistakes in their programms.
| When we compile a code, we must be sure, that the user's sourcecode will not cause damages in our program.
| To protect our program, in file named **error.py** there are some functions that raise errors in the most forbidden situations:

- **UnsupportedLangError** : user tries to select language that is not supported by the dockerfile (other than C, Cpp, Go, Java, Py3)
- **InvalidPathError** : user tries to get access to task, input or other file which does not exist
- **PathTooLangError** : to ensure safety and speed of the program, the path shouldn't be too long, we set the maximum lengh to 255 characters
- **TimeoutError** : that error is raised when we think that the program compiles much more it should, that error protects us expecially by infinite loop
- **OutOfMemoryError** : that error protects us by using too much memory by the program
- **CompilationError** : error in compilation time for other reasons)

| Example of errors:

- **UnsupportedLangError** : user tries to solve a task in  **C#**  language
- **InvalidPathError** : users tries to save file as **abc.def.ghi.jks.c**
- **TimeoutError** : time of user's sourcecode compile breaks maximum allowed time for the task, for example: 512 ms
- **OutOfMemoryError** : memory in compile time of user's sourcecode breaks maximum allowed memory, for example: 512 m
- **CompilationError** : variable a was used in the program and it was not declared or defined
- **PathTooLangError** : user tries to use path of length 301 characters

.. automodule:: runner.error
   :members:
   :undoc-members:
   :show-inheritance:

runner.runner module
--------------------

| `runner.py source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/runner/runner.py>`_
|
| Lang is the class that contains fields and functions for selecting the programming language of the task by logged in user, selecting task, compiling its by Docker file and checking results.
| The function   `get_dockerfile_dir <../html/runner.html#runner.runner.get_dockerfile_dir>`_   is used to get access to Docker to all available languages (C, C++, Go, Java, Python3).

| Function   `from_file <../html/runner.html#runner.runner.from_file>`_   is used to check if user selects an available programming language. It is important that codefpath must not have more than 255 characters and in otherwise the function raise error. The function would raise error too if we would try to check unavailable language. 

| That class collaborate with files from directories named `dummy` and `alghorithm` that are in the common directory at the same level with file named runner.py. In these directories we may find examples correct and failed implementation of all tasks. Failed implementation of tasks have end of file name `_false`.

Example: 

- algorithm_gcd.c : correct implementation
- algorithm_gcd_false.c : failed implementation

| The function named   `soSorryYouLose <../html/runner.html#runner.runner.soSorryYouLose>`_   is the most important function is the file. This function uses all of other functions in the file to check language, get access to Docker file, compile source code and return results of the code.
| This function also controls if the file was compiled in time_limit and if memory_limit was not broken. If time_limit or memory_limit was broken, the function raises error.  

| Then results are compared with the results from the database. If every results are equal, then anser is true, false otherwise.



.. automodule:: runner.runner
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: runner
   :members:
   :undoc-members:
   :show-inheritance:
