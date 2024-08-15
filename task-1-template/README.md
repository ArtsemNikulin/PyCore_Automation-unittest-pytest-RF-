# E-Learning Robot Framework Task 1: User Keywords
### Ground rules
1. Do not implement any other keywords beside those you are provided with.
2. Do not create any new files; they have been prepared in advance.
3. The passing score for this task is 100.

### Task description
For this task you will be using the provided `keywords.robot` file,
which contains a set of keywords for you to implement.

Please, read the documentation for each keyword carefully and implement it accordingly,
replacing the `No operation` placeholder with your implementation. For example:
```robotframework
*** Keywords ***
Concatenate varargs
    [Documentation]    The keyword should take a variable number of positional arguments into the list 'args'.
    ...                The keyword should log a following message when called: "Got args=<values>"
    ...                For example: "Got args=['first', 'second']"
    ...                Logs should appear in the console.
    ...                The keyword should return a string made of space-separated arguments it received.
    ...                For example: "first second"
    ...                Hint: use the 'Catenate' keyword from the BuiltIn library, or extended variable syntax.
    No operation
```

### Task outcomes
While working on this task, you will practice the following:
* Passing arguments to keywords.
* Returning values from keywords.
* Using variables.
* Using control flow structures.
* Using keywords from the [BuiltIn](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html) library.

### Checking your task
The keywords you implement will be used in a test suite. There will be a separate test case
for each of the keywords you implement. If the test case fails, you'll get an error message
describing the reason for the failure. along with the output from Robot Framework.