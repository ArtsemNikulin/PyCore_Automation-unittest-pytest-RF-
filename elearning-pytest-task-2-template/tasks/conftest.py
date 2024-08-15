def pytest_collection_finish(session):
    long_tests_count = len([i for i in session.items if i.get_closest_marker(name='long_running')])
    quick_tests_count = len(session.items) - long_tests_count
    print(f"Collected quick tests: {quick_tests_count}, long-running tests: {long_tests_count}")
