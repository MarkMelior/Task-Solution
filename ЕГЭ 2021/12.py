# Какая строка получится в результате применения приведённой ниже
# программы к строке. состояшей из 70 идуших подряд пифр 8? В ответе
# запишите полученную строку.

# НАЧАЛО
# ПОКА нашлось (2222) ИЛИ нашлось (3888)
# ЕСЛИ нашлось (2222)
# ТО заменить (2222. 83)
# ИНАЧЕ заменить (8888. 22
# КОНЕЦ ЕСЛИ
# КОНЕЦ ПОКА
# КОНЕЦ



s = '8' * 70 # 8 70 раз подряд
while '2222' in s or '8888' in s:
    if '2222' in s:
        s = s.replace('2222','88',1)
    else:
        s = s.replace('8888','22',1)
print(s)
