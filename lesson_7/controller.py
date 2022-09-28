import calc
import ui
import logging

def check(s):
    # в юи
    """ проверка возможности преобразования строки в комплекс и флоат, возвращает тру и преобразованное число если удалось, если нет то фолс"""
    try:
        float(s)
        return True, float(s)
    except ValueError:
        try:
            complex(s)
            return True, complex(s)
        except ValueError:
            print ('это не комплекс и не рациональное число')
            return False

def inp():
    # в юи
    """ ввод числа, берет строку, вертит цикл пока она не преобразуется в число, возвращает преобразованное число"""
    s = input("введи число - ")
    while not check(s):
        s = input("введи число - ")
    return check(s)[1]

def button():
    a = 0
    while a != "5":
        a = input("введи а (1 сложить, 2 вычесть, 3 умножить, 4 поделить, 5 выйти) ") # вызвать из юи
        x = 0
        y = 0
        data = ""
        if a == "1": 
            x = inp() # вызываем из юи
            y = inp() # вызываем из юи
            data = str(f'{x} + {y} = {calc.sum(x, y)}')
            print(data) # !!! ПРИ СБОРКЕ УБРАТЬ
            #put_in_log.logging(data)) # отдали дату в лог
            #print_data.ui(data) # отдали дату в юи
        if a == "2": 
            x = inp()
            y = inp()
            data = str(f'{x} - {y} = {calc.sub(x, y)}')
            print(data) # !!! ПРИ СБОРКЕ УБРАТЬ
            #put_in_log.logging(data)) # отдали дату в лог
            #print_data.ui(data) # отдали дату в юи
        if a == "3": 
            x = inp()
            y = inp()
            data = str(f'{x} * {y} = {calc.mult(x, y)}')
            print(data) # !!! ПРИ СБОРКЕ УБРАТЬ
            #put_in_log.logging(data)) # отдали дату в лог
            #print_data.ui(data) # отдали дату в юи
        if a == "4": 
            x = inp()
            y = inp()
            data = str(f'{x} / {y} = {calc.div(x, y)}')
            print(data) # !!! ПРИ СБОРКЕ УБРАТЬ
            #put_in_log.logging(data)) # отдали дату в лог
            #print_data.ui(data) # отдали дату в юи
    else:
        print("goodbye!")
        exit()

button() # вызывать из майна