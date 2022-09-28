import check

def get_input_number(serial_number = ''):
    """ 
    Функция получения строки (числа) от пользователя и преобразования его в число. 
    Возвращает преобразованное число.
    """
    number = input(f'Введите {serial_number} число - ')
    while not check(number):
        number = input(f'Введите {serial_number} число - ')
    return check(number)[1]






