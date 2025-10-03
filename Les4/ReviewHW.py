# Home work
# Задание 5. Создайте переменную text, значение которой определяется с помощью ввода данных с
# клавиатуры. Создайте переменную length - минимальная длина слова, определяемая с помощью
# ввода данных с клавиатуры. Выведите список со всеми словами, чья длина больше length

# вариант ввода отдельными словами
length = int(input("Введите минимальную длину слова:"))
text = input("Введите любое слово:")
list = []
while len(text) > length:
    list.append(text)
    text = input("Введите любое слово:")
    if len(text) > 0 and len(text) < length:
        print("Длина слова", text, "меньше минимума")
        text = input("Введите любое слово:")
    elif len(text) == 0:
        break
print(list)

# вариант ввода предложениями
text = input("Enter any text:")
length = int(input("Введите минимальную длину слова:"))
signs = [' ', '-', ':', ',', '.', ';', '?', '!', '_', '-', "'", '"', '/', '&', '$', '@', '+']
word_list = []
word = ''
for i in text:
    if i not in signs:
        word += i
    elif i in signs:
        if len(word) > length:
            word_list.append(word)
            word = ''
print(word_list)

# Задание 2. Создайте переменную text, значение которой определяется с помощью ввода данных
# с клавиатуры. Выведите список, в котором каждое слово будет перевёрнуто.
text = input("Enter any text:")
signs = [' ', '-', ':', ',', '.', ';', '?', '!', '_', '-', "'", '"', '/', '&', '$', '@', '+']
word_list = []
word = ''
for i in text:
    if i not in signs:
        word += i
    elif i in signs:
            word_list.append(word[::-1])
            word = ''
if len(word) > 0:
    word_list.append(word[::-1])
print(word_list)

# Задание 3. 