users.serializers package
=========================

Submodules
----------

users.serializers.user\_serializer module
-----------------------------------------
| `user_serializer source code <https://github.com/eryktr/iwsoj/blob/master/iwsoj/users/serializers/user_serializer.py>`_
|
| User_Serializer and Meta from file **user_serializer.py** are very important classes in our project.
|
| Thanks to the functions in these classes, we can check creating and saving a new user.
|
| Before the registration UniqueValidator checks if the e-mail address matches the corresponding regular expression.

Method **create** is used to register a new user. There are four strings required to add user to database:

- **username**
- **first_name**
- **email**
- **password**.

| It is also possible to add some optional data like **last_name** .
| Field **username** must be unique and it's forbidden to add a second user with the same **username** .
|
| Before the registration attempt, make sure that you have defined a new running configuration as:
|
| **python3 iwsoj/manage.py runserver**
|
| If data from all required fields is correct, system try to register user.
|
| We use url path http://localhost:8000/api/register/  to register to the database. 

.. automodule:: users.serializers.user_serializer
   :members:
   :undoc-members:
   :show-inheritance:


Module contents
---------------

.. automodule:: users.serializers
   :members:
   :undoc-members:
   :show-inheritance:
