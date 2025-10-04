# задание 1
num_1 = 100
name = "Алексей"
first_number = 1
text = "Мой текст"
greetings = "Hi!"

# задание 2
first_name = "Сергей"
print('Привет, меня зовут', first_name)

# Способ 2
print(f"Привет, меня зовут {first_name}.")

# Способ 3
message = "Привет, меня зовут" + " " + first_name + "."
print(message)

# задание 3
first_name = input("Enter your name: ")
surname = input("Enter your second_name: ")
title_name = first_name.title()
title_surname = surname.title()
print("Привет, меня зовут", title_name, title_surname)

# Способ 2
print(f"Привет, меня зовут {name.title()} {surname.title()}.")

# задание 4
a = input("Enter any number:")
b = input("Enter any number:")
print("Сумма =", float(a) + float(b))