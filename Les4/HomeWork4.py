# Задание 1. Сгенерируйте список numbers, состоящий из чисел в диапазоне от 0 до 100
# включительно, которые делятся без остатка как на 2, так и на 3.
# Выведите список numbers на экран.
# Способ 1
numbers = []
for num1 in range(100):
    if num1 % 2 == 0 and num1 % 3 == 0:
        numbers.append(num1)
print(numbers)
# Способ 2
numbers = [num for num in range(100) if num % 2 == 0 and num % 3 == 0]
print(numbers)

# Задание 2. Имеется список items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99,
# 44.32, None]. Составьте новый список numbers, который содержит только целые числа (int) и
# вещественные числа (float) из списка items. Выведите на экран сумму чисел в numbers.
items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
numbers = []
sum = 0
for item in items:
    if type(item) == int or type(item) == float:
        numbers.append(item)
        sum += item
print(numbers)
print(f"Сумма всех чисел из списка = {sum}")