'''
Создание и вывод переменных
'''

age = 22
name = "Кирилл"
surname = "Кюркчи"
city = 'Подольск'
print(f"Меня зовут {name} {surname} . Мне {age} года . Я живу в городе {city}")

'''
Ввод и вывод переменных
'''

name = input("Как вас зовут? - ")
surname = input("Какая у вас фамилия? - ")
age = input("Какой ваш возраст? - ")
city = input("В каком городе проживаете ? - ")

# проверка на написание года , год  или лет .

if int(age) % 10 ==1 and age != "11":
    print(f"Вас зовут {name} {surname} . Вам {age} год . Вы из города {city} . ")
elif int (age) % 10 in [2,3,4] and age not in ["12","13","14"]:
    print(f"Вас зовут {name} {surname} . Вам {age} года . Вы из города {city} . ")
else:
    print(f"Вас зовут {name} {surname} . Вам {age} лет . Вы из города {city} . ")

