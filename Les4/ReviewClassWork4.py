# Class work
# Задание 1. Дан список list1 = [1, ’1’, 4, 7, ’’, 1, ‘word’, [1, 2, 3], 4]. Выведите список, в
# котором будут только уникальные элементы. Кавычки в списке придётся заменить самостоятельно.

list1 = [1, '1', 4, 7, '', 1, 'word', [1, 2, 3], 4]
uni_list = []
for i in list1:
    if i not in uni_list:
        uni_list.append(i)
print(uni_list)

# Задание 2. Создайте переменную text, значение которой определяется с помощью ввода данных с
# клавиатуры. Выведите список с длинами каждого слова в строке text. Слова в тексте разделяются
# с помощью пробелов и знаков препинания.
text = input("Enter any text:")
signs = [' ', '-', ':', ',', '.', ';', '?', '!', '_', '-', "'", '"', '/', '&', '$', '@', '+']
count_letters = []
count = 0
for c in text:
    if c not in signs:
        count += 1
    elif c in signs and count !=0:
        count_letters.append(count)
        count = 0
    else:
        print("В тексте непредвиденная ошибка")
        break
if count != 0:
    count_letters.append(count)
print(count_letters)
# Задание 3. Определите, является ли введенное пользователем слово палиндромом. Решите эту
# задачу используя списки и не используя функцию reverse или срезы.
text = input("Enter any word:")
word = list(text.lower())
long_word = len(word) // 2
palindrom = True
for i in range (long_word):
    if word[i] == word[(i+1)*(-1)]:
        continue
    else:
        print("Слово", text, "НЕ ПАЛИНДРОМ")
        palindrom = False
        break
if palindrom:
    print("Слово", text, "ПАЛИНДРОМ")
# Задание 4. Создайте переменную - количество элементов в списке, которая определяется с
# помощью ввода данных с клавиатуры. Создайте список, который будет заполнен с помощью ввода
# значений с клавиатуры. Создайте ещё одну переменную - желаемый сдвиг списка, которая
# определяется с помощью ввода данных с клавиатуры. Сдвиньте имеющийся список вправо и влево
# на указанное число символов.
elements_count = int(input("Введите целое число:"))
first_list = []
for i in range(elements_count):
    first_list.append(i)
displacement = int(input("Введите смещение для списка:"))
list_plus2_disp = first_list.copy()
list_minus2_disp = first_list.copy()
# смещаем вправо
for i in range(displacement):
    temp = list_plus2_disp.pop()
    list_plus2_disp.insert(0, temp)
# смещаем влево
for i in range(displacement):
    temp = list_minus2_disp.pop(0)
    list_minus2_disp.append(temp)
print(first_list)
print(list_plus2_disp)
print(list_minus2_disp)