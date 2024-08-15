# eLearning Pytest Task 2: Hooks
## Ground rules:
1. Don not create or modify any test files, they have been prepared for you.
2. You can freely change `conftest.py` and `pytest.ini`
3. The task pass score is 100.

## Part 1
In provided test module some long-running tests have been marked as "long_running". Tests without this mark are known as quick.
Implement collection hook for calculating and printing tests marks in the following format:

```
Collected quick tests: {quick_tests_count}, long-running tests: {long_tests_count}
```

## Part 2
Update `pytest.ini` file in order to fix all markers related warnings during the pytest run. Here's an example:
```text
PytestUnknownMarkWarning: Unknown pytest.mark.long_running - is this a typo?
```