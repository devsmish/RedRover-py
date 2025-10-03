# Class work
# Задание 1. Дан список list1 = [1, ’1’, 4, 7, ’’, 1, ‘word’, [1, 2, 3], 4]. Выведите список, в
# котором будут только уникальные элементы. Кавычки в списке придётся заменить самостоятельно.
list1 = [1, '1', 4, 7, '', 1, 'word', [1, 2, 3], 4]
unilist = []
for i in list1:
    if i not in unilist:
        unilist.append(i)
print(unilist)

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
# Задание 4. 