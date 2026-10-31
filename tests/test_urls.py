from tinylib import parse_query, parse_url


def test_parse_query():
    assert parse_query("a=1&b=2") == {"a": "1", "b": "2"}


def test_parse_url_strips_spaces():
    assert parse_url(" https://a.com/b ")["scheme"] == "https"
