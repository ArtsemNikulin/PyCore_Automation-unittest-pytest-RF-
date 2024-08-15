# E-Learning Robot Framework Task 2: User libraries
### Ground rules:
1. Do not implement any other keywords beside those you are provided with.
2. Do not create any new files; they have been prepared in advance.
3. To complete this task successfully, you must earn a score of 100.

### Task description
For this task you will be using the provided file `ClassLibrary.py`, which requires you
to implement the set of keywords from Task 1, this time in a Python class.

Please, read the docstring for each method carefully and implement it accordingly.
For example:
```python
class ClassLibrary:
    def __init__(self, ):
        """The library should accept one required argument, 'name', and store it as instance
        attribute 'name' (e.g. self.name)."""

    def my_name_is(self, ):
        """
        The keyword should accept a positional argument 'surname' with a default value of None.
        The keyword should access the value given as an argument to the library - 'name'.
        The keyword should log a following message when called: "Got name=<name>, surname=<surname>"
        For example: "Got name=James, surname="
        Logs should appear in the console.
        Use the robot.api.logger API provided by Robot Framework.
        The keyword should return a string "My name is <name>" if 'surname' is None,
        or "My name is <surname>, <name> <surname>" if 'surname' was given.
        For example: "My name is James"; "My name is Bond, James Bond"
        """
```

### Task outcomes
While working on this task, you will practice the following:
* Using the Robot Framework library API.
* Calling Robot Framework APIs from a Python module.
* Implementing keywords as class methods.

### Checking the task
The keywords you implement will be used in a test suite. There will be a separate test case
for each of the keywords you implement. If the test case fails, you'll get an error message
describing the reason for the failure. along with the output from Robot Framework.