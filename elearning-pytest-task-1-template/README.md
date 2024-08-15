# eLearning Pytest Task 1: Fixtures
## Ground rules:
1. Do not implement any other functions or fixtures in template files besides ones instantiated.
2. Do not import any other packages, functions or variables besides these that are imported.
3. Keep test data in the corresponding test functions, do not store it externally.
4. Follow interfaces that are prepared for you, do not modify them.
5. Please, apply `@pytest.fixture()` decorators where needed - just keep them in one line.
6. The task pass score is 100.

## Part 1
1. Implement fixture 'connection' in session scope for sqlite3 connection to db in file 'example.db'. Put in fixture setup the following:    
    ```
    connection = sqlite3.connect('example.db')
   ```
2. Add teardown for connection closing should contain the following::
    ```python
    connection.close()
    ```
3. Create fixture 'cursor' in session scope with 'connection' fixture as parameter. This fixture should return cursor object from connection:
    ```python
    connection.cursor()
    ```

## Part 2

1. Implement fixture 'table_cursor' in function scope based on 'cursor' fixture.
2. Parametrize this fixture by 'table_data' variable. Hint: use 'params' fixture argument.
3. Create several steps in setup to prepare table items:
    ```python
    cursor.execute('drop table if exists items')
    cursor.execute('create table items (id int, name text)')
    ```
4. Insert data from fixture parameters in table:
    ```python
    cursor.execute(f'insert into items values  {request.param}')
    ```
5. Commit the change:
    ```python
    cursor.connection.commit()
    ```
6. Return the cursor;
7. And drop the table in teardown:
    ```python
    cursor.execute('drop table if exists items')
    ```

## Part 3
1. Implement test to verify data in table using 'table_cursor' fixture. 
2. It is required to compare 'table_data' variable with data from 'items' table using the next construction:  
    ```python
    table_cursor.execute('select id, name from items')
    ```
3. **Please keep test data for the test inside test function! Do not import it from conftest.py or store outside of the function. Follow ground rules #3 and #4.**
