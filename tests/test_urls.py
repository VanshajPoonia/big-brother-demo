from tinylib import parse_query


def test_parse_query():
    assert parse_query("a=1&b=2") == {"a": "1", "b": "2"}
