'''
Найти сумму чисел по формуле n+nn+nnn
'''

'''
Первый способ
'''
number = input("Введите число : -")
summa = int(number)+int(number+number)+int(number+number+number)
print(f"Сумма чисел по формуле n+nn+nnn .Равна {int(number)}+{int(number+number)}+{int(number+number+number)}={summa}")

''''
Второй способ
'''

number = input("Введите число : -")
n = int(number)
nn = int(number+number)
nnn = int(number+number+number)
suma = n + nn + nnn
print(f"Сумма чисел по формуле n+nn+nnn .Равна {n}+{nn}+{nnn}={suma}")