import calc
import ui
import logger

def button_menu():
    '''
    В зависимости от входящей команды выполняет вычисления с числами
    ''' 
    while True:
        x = 0
        y = 0
        command = input("Введите номер команды (1 сложить, 2 вычесть, 3 умножить, 4 поделить, 5 посмотреть журнал вычислений, 6 выйти) - ")
        if command == "6":
            print("До свидания!")
            exit()
        elif command in "1234":
            x = ui.get_input_number("первое") 
            y = ui.get_input_number('второе') 
        if command == "1": 
            logger.write_log(ui.view_result(str(f'{x} + {y} = {calc.sum(x, y)}')))
        elif command == "2": 
            logger.write_log(ui.view_result(str(f'{x} - {y} = {calc.sub(x, y)}')))
        elif command == "3": 
            logger.write_log(ui.view_result(str(f'{x} * {y} = {calc.mult(x, y)}')))
        elif command == "4": 
            logger.write_log(ui.view_result(str(f'{x} / {y} = {calc.div(x, y)}')))
        elif command == "5": 
            print(logger.read_logs())
        else:
            print('Вы ввели неверную команду!')
        