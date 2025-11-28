from src.lib.text import normalize, tokenize, count_freq, top_n
import pytest

# запуск через: pytest -q --disable-warnings --maxfail=1

# @pytest.mark.parametrize("text, expected", [
#         ("ПрИвЕт\\nМИр\\t", "привет мир"),
#         ("ёжик, Ёлка", "ежик, елка"),
#         ("Hello\\r\\nWorld", "hello world"),
#         ("  двойные   пробелы  ", "двойные пробелы"),
#     ])
# def test_normalize(text,expected):
#     assert normalize(text) == expected


# @pytest.mark.parametrize("text, expected", [
#     ("привет, мир!", ["привет", "мир"]),
#     ("Hello, World!!!", ["Hello", "World"]),
#     ("по-настоящему круто", ["по-настоящему", "круто"]),
#     ("2025 год!", ["2025", "год"]),
#     ("emoji 😀 не слово!", ["emoji", "не", "слово"]),
# ])
# def test_tokenize(text, expected):
#     assert tokenize(text) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["c", "b", "a", "c", "b", "a"], {"a": 2, "b": 2, "c": 2}),
        (["bb", "aa", "bb", "aa", "cc"], {"aa": 2, "bb": 2, "cc": 1}),
        (["c", "b", "c", "c", "b", "a"], {"c": 3, "b": 2, "a": 1}),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "freq, n,expected",
    [
        ({"c": 2, "b": 2, "a": 2}, 3, [("a", 2), ("b", 2), ("c", 2)]),
        ({"bb": 2, "aa": 2, "cc": 1}, 2, [("aa", 2), ("bb", 2)]),
        ({"x": 5, "y": 5, "a": 5}, 3, [("a", 5), ("x", 5), ("y", 5)]),
        ({"x": 5, "y": 5, "a": 5}, 1, [("a", 5)]),
    ],
)
def test_top_n(freq, n, expected):
    assert top_n(freq, n=n) == expected
