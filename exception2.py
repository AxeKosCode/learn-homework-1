"""
Домашнее задание №1
Исключения: приведение типов
* Напишите функцию get_summ(num_one, num_two), которая принимает 
  на вход два целых числа (int), складывает их и возвращает результат 
  сложения
* Оба аргумента нужно приводить к целому числу при помощи int() и 
  перехватывать исключение ValueError если приведение типов не сработало
    
"""

def get_summ(num_one, num_two):
    """
    Замените pass на ваш код
    """
    try:
        one = int(num_one)
    except ValueError:
        return 'Первый аргумент должен быть числом!'
    try:
        two = int(num_two)
    except ValueError:
        return 'Второй аргумент должен быть числом!'
    
    return one + two

    
if __name__ == "__main__":
    print(get_summ(2, 2))
    print(get_summ(3, "3"))
    print(get_summ("4", "4"))
    print(get_summ("five", 5))
    print(get_summ("six", "шесть"))
    print(get_summ(10, "ten"))