# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# 0.56 -> 11

print("Программа, которая принимает на вход вещественное число и показывает сумму его цифр.")
stringNumber = input("Введите число: ").replace("-", "").replace(".", "")
result = 0

for i in range(len(stringNumber)):
    result += int(stringNumber[i])

print(f'result = {result}')