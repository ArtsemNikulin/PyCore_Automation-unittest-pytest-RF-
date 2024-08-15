from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    filtered_data = []

    for js in data:
        if all(f(js) is not None for f in filters):
            filtered_data.append(selector(js))

    return filtered_data




def select(*columns: str) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    def get_columns(data):
        result = {i: data.get(i) for i in columns}
        return result

    return get_columns


def field_filter(column: str, *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""

    def filtering(data):
        if data[column] in [i for i in values]:
            return data

    return filtering


def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
        {'name': 'Emily', 'gender': 'female', 'sport': 'Volleyball'},
    ]

    value = query(
        friends,
        select('name', 'gender'),
        field_filter('name', *('Emily', 'Sam')),
        field_filter('gender', *('female',))
    )
    assert [{'gender': 'female', 'name': 'Emily', 'sport': 'Volleyball'}] == value


if __name__ == "__main__":
    test_query()
