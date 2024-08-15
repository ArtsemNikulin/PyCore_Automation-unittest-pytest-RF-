# eLearning Unittest Task 2: Mocks

## Ground rules:
1. Do not import any other packages besides those that have been already imported.
2. Follow the interfaces that have been prepared for you, do not modify them.
3. Perform class initialization in setUp.
4. The task pass score is 100.
5. **Important note**: `Unexpected success` error message means that you are most likely modified template files you were not supposed to modify. Please check with the task description once again.

## Task description

1. In tests/test_converter.py implement the `mock_converter` function, that will be used to `mock` actual method later in the code:
     ```python
     def mock_converter(_, celsius):
          """Docstring."""
          pass
     ```
The signature should take a Celsius argument and return a Fahrenheit result. First argument marked `_` should not be changed.

2. Implement the `test_converter` test case and apply a `unitetest.mock.patch()` decorator for the implemented function, so that it will use the mock_converter function instead of the original one: 
     ```python
     @patch() # Apply proper arguments here
     def test_converter(self):
          """Docstring."""
          # Implement your test case here
          pass
     ```

3. Add and change the docstrings whereever needed.

Expected result:
- `mock_converter` function implemented.
- A test case that uses the patched converter method is implemented.
- Docstrings added/changed whereever needed.
