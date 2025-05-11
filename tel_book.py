Tel_book = {
    79121 : "Alex" ,
    79122 : "Pavel" ,
    79123 : "Petr" ,
    79124 : "Stas"
    }
print ("""
    1. Добавить контакт
    2. Удалить контакт
    3. Найти контакт
    4. Показать все контакты
    5. Выход  """)
Activ = True
while Activ:
    try:
        select = int(input())
    except ValueError:
        print("Введите число от 1 до 5")
        continue  
    if select == 1 :
        print ("Введите имя")
        name = input()
        print("Введите номер контакта")
        number = input()
        Tel_book[name] = number
        print(f"Контакт {name} добавлен")
    elif select == 2:
        print("Введите имя контакта")
        name = input()
        if name in Tel_book :
            del Tel_book[name]
            print (f"Контакт {name} удалён")
        else :
            print ("Контакт не найден")
    elif select == 3 :
        print("Введите имя")
        name = input()
        if name in Tel_book :              
            print(f"Номер контакта {name} : {Tel_book[name]}")
        else :
            print("Контакт не найден")
    elif select == 4 :
        print (Tel_book)
    elif select == 5 :
        Activ = False
    else :
        print ("Неверный ввод")        