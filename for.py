"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
classes = [ {'school_class': '2a', 'scores': [5, 4, 5, 5, 4]},
            {'school_class': '2c', 'scores': [4, 4, 4, 5, 4, 3]},
            {'school_class': '3a', 'scores': [3, 3, 4, 3, 5]},
            {'school_class': '3b', 'scores': [5, 3, 4, 2, 2, 2, 3]},
            {'school_class': '4a', 'scores': [3, 4, 5, 5, 5, 3]}
         ]

class_average = {}

def school_average_mark(dict_of_average_marks):
    '''Возвращает средний балл по школе
    Аргумент подавать в виде словаря средних оценок всех классов
    '''
    result = 0
    for average in dict_of_average_marks.values():
        result += average
    return result / len(dict_of_average_marks)


def class_average_mark(list_of_scores):
    '''Возвращает средний балл по классу
    Аргумент подавать в виде списка оценок класса
    '''
    return sum(list_of_scores) / len(list_of_scores)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    for cl in classes:
        class_average[cl['school_class']] = round(class_average_mark(cl['scores']), 1)
    # print(class_average)

    print(f'Средний балл по школе составляет: {round(school_average_mark(class_average), 1)} \n')

    for k, v in class_average.items():
        print(f'Средний балл по классу {k} составляет: {v}')

    
if __name__ == "__main__":
    main()