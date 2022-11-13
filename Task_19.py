'''
19. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
'''
num = int(input('Введите искомое число: '))
my_list = ['qwer', 'asdf', '2456', '24', 'dpo', '7']

def find_number(my_list, number):
    return list(filter(lambda elem: str(number) in elem, my_list))

print(find_number(my_list, num))  # Выводим элемент, который содержит в себе искомое число, либо пустой список при его отсутствии.
