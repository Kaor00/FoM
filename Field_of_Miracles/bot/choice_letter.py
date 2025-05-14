from qq.data.use_letter import ultr


def fn(mass):
    """Возвращает самую популярную букву из массива букв,
    а также записывает эту букву в список использованных букв"""
    for i in mass:
        if i[0] not in ultr:
            ultr.append(i[0])
            return i[0]

