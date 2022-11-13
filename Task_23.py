'''
23. Напишите программу, которая найдёт произведение пар чисел списка. 
    Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15].
'''
my_list = [2, 3, 4, 5, 6]
print(f'Список: {my_list}')

def Product_Pairs_Numbers(list):
    return [list[i] * list[len(list) - 1 - i] for i in range(len(list) // 2 + len(list) % 2)]

print(f'Произведение пар чисел = {Product_Pairs_Numbers(my_list)}')
