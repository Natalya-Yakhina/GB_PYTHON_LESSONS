'''Задание с семинара
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,. приоритет операций стандартный.
Дополнительное задание: Добавьте возможность использования скобок, меняющих приоритет операций
*Пример:
2+2 => 4;
1+2*3 => 7;

10/2*5 => 25;
10 * 5 * => недостаточно числовых данных
-5 + 5 => 0
два + три => неправильный ввод: нужны числа
(2+((5-3)*(16-14)))/3 => 2
(256 - 194 => некорректная запись скобок'''


symbols = ['+', '-', '*', '/', '(', ')']

expression = input('Введите математическое выражения для расчёта: ')

sub_expression = ''

def brackets_checking(input_text):
    result_list = []
    count1 = 0
    count2 = 0 
    for ch in input_text:
        if ch == '(':
            count1 += 1
        elif ch == ')':
            count2 += 1     
    if count2 != count1:
        print(f'Некорректная запись скобок в выражении -> {input_text}')
        result_list.append(False)
    else: result_list.append(True).append(count1)
    return result_list



if expression.__contains__('('):
    check_brackets = brackets_checking(expression)
    if (check_brackets[0]):
        input_brackets_count = check_brackets[1]
        split_string = expression.split('(')[input_brackets_count - 1].split(')')[0]

