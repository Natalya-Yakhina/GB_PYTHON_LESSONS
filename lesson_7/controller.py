import calc
import ui
import logging

def button_menu():
    command = 0
    while command != "5":
        command = input("Введите номер команды (1 сложить, 2 вычесть, 3 умножить, 4 поделить, 5 выйти) - ")
        x,y = 0
        if (command in "1234"):
            x = ui.get_input_number("первое") 
            y = ui.get_input_number('второе') 
        data = ""
        if command == "1": 
            data = str(f'{x} + {y} = {calc.sum(x, y)}')
            # put_in_log.logging(data)) # отдали дату в лог
            #print_data.ui(data) # отдали дату в юи
        elif command == "2": 
            data = str(f'{x} - {y} = {calc.sub(x, y)}')
            #put_in_log.logging(data)) # отдали дату в лог
            #print_data.ui(data) # отдали дату в юи
        elif command == "3": 
            data = str(f'{x} * {y} = {calc.mult(x, y)}')
            #put_in_log.logging(data)) # отдали дату в лог
            #print_data.ui(data) # отдали дату в юи
        elif command == "4": 
            data = str(f'{x} / {y} = {calc.div(x, y)}')
            #put_in_log.logging(data)) # отдали дату в лог
            #print_data.ui(data) # отдали дату в юи
        elif command == "5":
            print("goodbye!")
            exit()
        else:
            print('Вы ввели неверную команду!')