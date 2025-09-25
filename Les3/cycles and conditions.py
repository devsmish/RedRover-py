# Задание 1
n = int(input("Enter any number: "))
if n % 2 == 0:
    print("Число", n, "четное")
else:
    print("Число", n, "не четное")

# Задание 2
day = input("Enter the day:")
if day in ("суббота", "воскресение"):
    print("Сегодня выходной день!")
elif day == "среда":
    print("Мне сегодня к стоматологу в 15:30.")
elif day in ("понедельник", "вторник", "четверг", "пятница"):
    print("Сегодня обычный день.")
else:
    print("Вы ввели неправильное название!")

# Задание 3
n = int(input("Enter any number: "))
text = input("Enter any text: ")
for _ in range(n):
    print(text)

# Задание 4
message = input("Enter any text: ")
count = 0
for c in message:
    if c in ("а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"):
        count = count + 1
        print(c, "гласная")
    else:
        print(c, "согласная")
print("Всего гласных букв:", count)

# Задание 5
sum = 0
a = 0
while a>=0:
    a = float(input("Enter any number: "))
    if a % 1 == 0:
        sum = sum + a
    else:
        print("Вы ввели дробное число. Программа прерывает работу")
        break
print("Сумма введенных чисел =", sum)