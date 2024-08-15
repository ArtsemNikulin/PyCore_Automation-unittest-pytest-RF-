import pytest


@pytest.mark.duration('short')
def test_feature1():
    assert 1


@pytest.mark.critical
def test_feature2():
    assert True


def test_feature3():
    assert -1


@pytest.mark.long_running
def test_feature4():
    ...
    assert True
