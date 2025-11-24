from src.lib.text import normalize, tokenize, count_freq, top_n
import pytest

@pytest.mark.parametrize("text, casefold, yo2e, expected", [
    ("Hello, World!", True, True, "Hello, World!"),
    ("Hello, World!", False, True, "Hello, World!"),
    ("Hello, World!", True, False, "Hello, World!"),
    ("Hello, World!", False, False, "Hello, World!"),
])  
def test_normalize(text, casefold, yo2e, expected):
    assert normalize(text, casefold=casefold, yo2e=yo2e) == expected

@pytest.mark.parametrize("text, expected", [
    ("Hello, World!", ["hello", "world"]),
    ("Hello, World!", ["Hello", "World"]),
    ("Hello, World!", ["Hello", "World"]),
    ("Hello, World!", ["Hello", "World"]),
    ("Hello, World!", ["Hello", "World"]),
])
def test_tokenize(text, expected):
    assert tokenize(text) == expected

@pytest.mark.parametrize("tokens, expected", [
    (["c", "b", "a", "c", "b", "a"], {"c":2, "b":2, "a":2}),
    (["bb", "aa", "bb", "aa", "cc"], {"bb":2, "aa":2, "cc":1}),
    (["a","b","a","c","b","a"], {"a":3, "b":2, "c":1}),
    (["a","b","a","c","b","a"], {"a":3, "b":2, "c":1}),
])
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected

@pytest.mark.parametrize("freq, n, expected", [
    ({"c":2, "b":2, "a":2}, 3, [("a", 2), ("b", 2), ("c", 2)]),
    ({"bb":2, "aa":2, "cc":1}, 2, [("aa", 2), ("bb", 2)]),
    ({"x":5, "y":5, "a":5}, 3, [("a", 5), ("x", 5), ("y", 5)]),
])
def test_top_n(freq, n, expected):
    assert top_n(freq, n=n) == expected
