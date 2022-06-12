'''
Ввод времени в секундах.
Отобразить в ввиде часов.
'''
second = int(input ("Введите количесетво секунд : - "))
hour = second // 3600
minute = second // 60 - hour * 60
sec= second - (minute * 60 + hour * 3600)
print(f"{'время':>12} {hour:02d}:{minute:02d}:{sec:02d}")