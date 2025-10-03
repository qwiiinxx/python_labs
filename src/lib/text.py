def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    s = text.strip()
    if casefold:
        s = s.casefold()
    
    if yo2e:
        s = s.replace('ё', 'е').replace('Ё', 'е')

    s = " ".join(s.split())
    return s

# print(normalize("ПрИвЕт\nМИр\t")) # "привет, мир"
# print(normalize("ёжик, Ёлка")) # "ежик, елка"
# print(normalize("Hello\r\nWorld")) # "hello world"
# print(normalize("  двойные   пробелы  ")) # "hello world"


def tokenize(text: str) -> list[str]:
    result = []
    word = ''
    for i, w in enumerate(text):
        if w.isalnum() or w == '_':
            word += w
        elif w == '-' and word and i + 1 < len(text) and text[i+1].isalnum():
            word += w
        else:
            if word:
                result.append(word)
                word = ''
    if word:
        result.append(word)
    return result

# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    