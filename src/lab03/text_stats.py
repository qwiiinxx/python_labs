import sys # НАЖАТЬ control + D
from lib import normalize
from lib import tokenize
from lib import count_freq
from lib import top_n

for line in sys.stdin:
    print(line.strip('\n'))

# Всего слов: <N>
# Уникальных слов: <K>
# Топ-5: — по строке на запись в формате слово:кол-во (по убыванию, как в top_n).
