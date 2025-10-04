# Задача 1
a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
c = int(input("Enter any number: "))
# Расчет среднего значения
print("Среднее значение =", (a +b +c)/3)

# Задача 2
celsius = float(input("Введите температуру в градусах Цельсия: "))
# Перевод градусов Цельсия в градусы Фаренгейта по формуле
print("Температура по Фаренгейту будет =", (9 / 5 * celsius + 32))

# Задача 3
a = float(input("Enter any number: "))
# Рассчитаем квадрат введенного числа
print("Квадрат числа", a , "равен", a * a)

# Задача 4
a = float(input("Enter any number: "))
b = float(input("Enter any number: "))
print("Сумма чисел", a, "и", b , "равна", a + b)
print("Разница чисел", a, "и", b , "равна", a - b)
print("Произведение чисел", a, "и", b , "равно", a * b)
print("Частное чисел", a, "и", b , "равно", a / b)
print("Целая часть от деления", a, "и", b , "равна", a // b)
print("Остаток от деления", a, "и", b , "равен", a % b)
