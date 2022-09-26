'''1- Определить, присутствует ли в заданном списке строк, некоторое число'''

list = ['123', 'cake', 'joo', '34', 'foo', 'Main', '89']

input_number = input('Введите число для поиска в списке: ')

boolean = False
for i in range(len(list)):
    if list[i] == input_number:
        print (f'Число {input_number} находится в списке под индексом {i}')
        boolean = True
        break


if (not boolean):
    print (f'{input_number} в списке не найдено!')
