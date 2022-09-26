'''5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.'''

digits = [123, 12, 65, 84, 25, 43, 86, 35, 90]

result = []

for i in range(int(len(digits)/2)):
    result.append(digits[i] + digits[len(digits)-1 - i])
if (len(digits) % 2 != 0):
    result.append(digits[int(len(digits)/2)])
print (result)