with open("text.txt", 'r') as file:  # Открываем файл, выдав имя file
    stroka = file.read()  # Читаем строку
slova = stroka.split()  # Делим строку на слова, записывая в список
unicum = list()  # Создаем новый список для уникальных слов
for slovo in slova:  # Для слова в словах
    if slovo in unicum:  # Если слово в списке для уникальных слов
        pass  # Ничего не делаем
    else:  # Или
        unicum.append(slovo)  # Записываем слово в список с уникальными словами
with open("output.txt", "w") as file:  # Открыв файл, даём ему имя file
    file.write("Список уникальных слов из text.txt: ")  # Записываем в файл текст
    for slovo in unicum:  # Для каждого слова в уникальном списке
        file.write(slovo + " ")  # Записать это слово в файл
