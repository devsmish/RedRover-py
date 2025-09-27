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