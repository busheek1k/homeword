''''
Найти большую цифру в числе
'''
while True:
    int_number = int(input("Введите целое положительное число : - "))
    if (int_number // 10 != 0 and int_number > 0) or 1 <= int_number <= 9:
        max_number = int_number % 10
        int_number = int_number // 10
        break
    else:
        print("Число не удовлетворено условию.")
        print("Введите заново число")

while int_number != 0 and max_number != 9:
    remender = int_number % 10
    if remender > max_number:
        max_number = remender
    int_number = int_number // 10

print(f"Максимальное число равно : {max_number}")
