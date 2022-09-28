import check
import controller
import logger

def get_input_number(serial_number = ''):
    """ 
    Функция получения строки (числа) от пользователя и преобразования его в число. 
    Возвращает преобразованное число.
    """
    number = input(f'Введите {serial_number} число - ')
    while not check.check_number(number):
        number = input(f'Введите {serial_number} число - ')
    return check.check_number(number)[1]

def get_command():
    """ 
    Функция получения строки (числа) от пользователя как команды. 
    """
    while True:
        command = input("Введите номер команды (1 сложить, 2 вычесть, 3 умножить, 4 поделить, 5 посмотреть журнал вычислений, 6 выйти) - ")
        if command == "6":
            view_result("До свидания!")
            exit()
        elif command in "1234":
            x = get_input_number("первое") 
            y = get_input_number('второе') 
            controller.button_menu(command, x, y)
        elif command == "5":
            print(logger.read_logs())
        else:
            print('Вы ввели неверную команду!')


def view_result(result):
    '''
    Выводит на экран строку из аргумента
    '''
    print(result)
    return result


