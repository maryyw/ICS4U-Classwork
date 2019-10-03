from list_functions import insert_at, insert, remove_at


def test_insert_at():
    original = [1, 2, 3, 4]
    expected = [1, 2, 5, 3, 4]
    result = insert_at(original, 5, 2)
    assert result == expected


def test_insert():
    original = [1, 2, 5, 6]
    expected = [1, 2, 3, 5, 6]
    result = insert(original, 3)
    assert result == expected

    original = [1, 2, 5, 6]
    expected = [1, 2, 5, 6, 7]
    result = insert(original, 7)
    assert result == expected


def test_remove_at():
    original = [1, 2, 3, 4]
    expected = [1, 3, 4]
    result = remove_at(original, 2)
    assert result == expected