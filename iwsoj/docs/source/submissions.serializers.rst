submissions.serializers package
===============================

Submodules
----------

submissions.serializers.submission\_serializer module
-----------------------------------------------------
| `submission_serializer source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/submissions/serializers/submission_serializer.py>`_
|
| The function named **create** from class named SubmissionSerializer is used to create a new submission and add it to the database.

| The method requires fields:

- **sourceCode** : the code which was written by a user, TEXT type
- **task** : id number of the selected task, INT type
- **language** : programming language selected by a user, TEXT type
- **user** : id number of the user, INT type

If the method return correct object, it is added to the database.

.. automodule:: submissions.serializers.submission_serializer
   :members:
   :undoc-members:
   :show-inheritance:


Module contents
---------------

.. automodule:: submissions.serializers
   :members:
   :undoc-members:
   :show-inheritance:
