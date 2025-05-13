vvod =(input().strip())
try:
    result = eval(vvod)
    print (f"Результат : {result}")
except ZeroDivisionError:
    print ("Ошибка делеления на ноль")
except NameError:
    print("Неверный ввод")        