# Задача 1. Создайте переменную word, значение которой определяется через ввод данных
# с клавиатуры. Программа должна вывести количество гласных и согласных букв в введенной
# строке.
import sys
from tkinter.scrolledtext import example

vowels_kir = "уеыаоэёяиюУЕЫАОЭЁЯИЮ"
consonants_kir = "йцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБ"
vowels_lat = "eyuioaEYUIOA"
consonants_lat = "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM"
word = input("Enter any word:")
count_vow = 0
count_cons = 0
for letter in word:
    if letter in vowels_kir or letter in vowels_lat:
        count_vow += 1
    elif letter in consonants_kir or letter in consonants_lat:
        count_cons += 1
    else:
        print(letter, "- это служебный символ")
print("Гласных букв:", count_vow)
print("Согласных букв", count_cons)

# Задача 2. Напишите программу которая выводит шаблонное приветствие в зависимости от
# введённого пользователем времени суток. Если время с 00:00 до 06:00 часов нужно вывести
# “Доброе утро”, если время с 06:00 до 12:00 часов нужно вывести “Добрый день”, если время
# с 12:00 до 18:00 часов нужно вывести “Добрый вечер”, если время с 18:00 до 00:00 часов нужно
# вывести “Доброй ночи”.
import sys
time = float(input("Enter current time:"))
if time % 1 != 0 or time > 24:
    print("Время введено не верно!")
    sys.exit()
elif time >=0 and time < 6:
    print("Доброе утро!")
elif time >=6 and time < 12:
    print("Добрый день!")
elif time >=12 and time < 18:
    print("Добрый вечер!")
elif time >=18 and time < 24:
    print("Доброй ночи!")
else:
    sys.exit()

# Задача 3. Создайте переменную num, значение которой определяется через ввод данных с
# клавиатуры. Программа должна вывести сумму всех чисел до этого числа включительно.
# Попробуйте решить разными способами.
while True:  # бесконечный цикл
    num = float(input("Enter an integer number: "))

    if num % 1 != 0 and num < 0:  # проверяем, целое ли число
        print("You have entered incorrect data! Try again.")
        continue  # возвращаемся в начало цикла
    else:
        result = 0
        num = int(num)  # теперь точно целое, можно перевести в int
        while num > 0:
            result = result + num
            num = num - 1
        print("Сумма всех чисел =", result)
        break  # завершаем цикл после успешного ввода

# Способ 2
num = int(input("Enter an integer number: "))
sum = 0
for i in range(1, num+1):
    sum += i
print(f"Сумма всех чисел по способу 2 = {sum}")

# Способ 3
num = int(input("Enter an integer number: "))
sum = 0
while num !=0:
    sum += num
    num -= 1
print(f"Сумма всех чисел по способу 3 = {sum}")

# Задача 4. Напишите программу, которая в последовательности натуральных чисел определяет
# максимальное число, кратное 5. Программа получает на вход количество чисел в последовательности,
# а затем сами числа. В последовательности всегда имеется число, кратное 5. Программа должна
# вывести одно число - максимальное число, кратное 5.
num = int(input("Enter an integer number: "))
max_num = 0
if num < 5:
    print("В последовательности нет чисел кратных 5")
elif num % 1 != 0:
    print("Введено дробное число!")
else:
    for i in range (num):
        if i % 5 == 0 and i > max_num:
            max_num = i
            i += 1
    print("Максимально кратное 5 число в последовательности =", max_num)

# Задача 5. Задание со *. Напишите калькулятор, который будет принимать 2 числа и знак.
# После чего программа должна произвести нужную математическую операцию и вывести
# результат. Пример: 21/3. Ответ: 7
calculation = input("Введите пример для двух чисел:")
operators = "+-*/"
num1 = ''
num2 = ''
operator = ''
for i in calculation:
    if i not in operators:
        if not operator:
            num1 += i
        else:
            num2 += i
    else:
        operator = i

num1 = int(num1)
num2 = int(num2)
if operator == '+':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == '-':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == '*':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == '/':
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("Операция не известна")