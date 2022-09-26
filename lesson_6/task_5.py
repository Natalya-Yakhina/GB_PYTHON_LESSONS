'''5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.'''

digits = [123, 12, 65, 84, 25, 43, 86, 35, 90]

result = digits[:2:]

print(result)

# for i in range(int(len(digits)/2)):
    # result.append(digits[i] + digits[len(digits)-1 - i])
# if (len(digits) % 2 != 0):
    # result.append(digits[int(len(digits)/2)])
# print (result)





# print(list(filter(lambda char: char.isdigit(), ['1', '2', 'f', '4'])))


# print(reduce(lambda element_1, element_2: element_1+element_2, [ord(char) for char in 'python']))