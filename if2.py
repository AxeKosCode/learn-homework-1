"""
Домашнее задание №1
Условный оператор: Сравнение строк
* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные параметры 
  и выводя на экран результаты
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(check_strings('hello', 'world'))  # None
    print(check_strings('hello', 5))        # 0
    print(check_strings('world', ''))       # 2
    print(check_strings('42', 'python'))    # None
    print(check_strings('python', 'learn')) # 2
    print(check_strings('hi', 'learn'))     # 3
    print(check_strings('', ''))            # 1
    print(check_strings('hi', 'hi'))        # 1
    print(check_strings('learn', 'Learn'))  # None
    


    
def check_strings(str1, str2):
    if not ((type(str1) == str) and (type(str2) == str)):
        return 0
    if str1 == str2:
        return 1
    if len(str1) > len(str2):
        return 2
    if str2 == 'learn':
        return 3
    # return 'Не соответстует ни одному условию'
        

if __name__ == "__main__":
    main()