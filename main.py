import math

try:
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    x = float(input("Введите x: "))
    try:
        if (x < 5):
                y = (6 * a * b) - (5 * x)
        else:
            y = (5 * (math.pow(a, 2) + math.pow(b, 2))) / (x - 4)
        print("Ответ: " + format(y, "#.2f"))
    except:
        print("Нет решения!")
except:
    print("Неверные входные данные!")
