"""
Домашнее задание №1
Цикл while: ask_user со словарём
* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:
    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

my_answers = {
    'привет' : 'Приветствую!',
    'hello' : 'Хэллоу!',
    'hi' : 'Хай!',
    'как дела' : 'Хорошо!',
    'что делаешь' : 'Программирую',
    'где ты живешь' : 'В твоём компьютере',
    'сколько тебе лет' : 'Я не веду такую статистику'
}

user_questions = []

def ask_user_dict():
    """
    Замените pass на ваш код
    """
    while True:
        question = input('  Спрашивай, что хочешь: ').lower().strip('?! ')
        # print(question)
        if question:
            if question == 'exit' or question == 'выход':
                print('До встречи!')
                break
            elif question in my_answers:
                print(my_answers[question])
            # elif question[:-1] in my_answers:
            #     print(my_answers[question[:-1]])
            elif question in user_questions:
                print('Ты вроде уже спрашивал это')
            else:
                user_questions.append(question)
                print('У меня нет ответа на этот вопрос')
        else:
            print('Ты ничего не спросил')
    # print('user_questions =', user_questions)


if __name__ == "__main__":
    ask_user_dict()