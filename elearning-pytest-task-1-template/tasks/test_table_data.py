def test_table_data(table_cursor):
    expected = table_data = [(1, "books")]
    actual = table_cursor.execute('select id, name from items').fetchall()

    assert expected == actual
