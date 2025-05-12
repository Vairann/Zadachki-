import random
chislo = list(str(random.randint(1000 , 9999)))
print (chislo)
APP = True
while APP :
    vibor = list(input())
    if len(vibor) > 4:
        print ("Введён неверный формат числа")
        break
    print (vibor)
    if vibor == chislo:
        print ("Вы угадали")
        APP = False
        break
    for i in range(4):
        if vibor[i] == chislo[i] :
            print (f"{i+1} цифра стоит правильно")
        elif vibor[i] in chislo:
            print(f"{i+1} цифра есть в числе но стоит не на своём месте")   
