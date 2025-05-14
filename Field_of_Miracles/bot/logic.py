from collections import Counter
import re
from qq.bot.choice_letter import fn

path = r'C:\Users\islam\PycharmProjects\try\Field_of_Miracles\data\russian.txt'


def lgk(w):
    """Поиск слова в словаре по его длинне с фильтрацией по маске,
    составление списка часто встречающихся букв"""
    s = "".join(w).replace("_", ".")
    with open(path, 'r', encoding='windows-1251') as f:
        russian_words = f.read().splitlines()

    pattern = f"^{s}$"
    russian_words = [i.lower() for i in russian_words if re.match(pattern, i)]

    all_letters = "".join(russian_words)
    letter_freq = Counter(all_letters.lower())

    ltr = fn(letter_freq.most_common(33))
    return ltr

