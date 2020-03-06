"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
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

def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
        try:
            question = input('  Спрашивай, что хочешь: ').lower().strip('?! ')
        except KeyboardInterrupt:
            print('   Пока!')
            break

        if question:
            if question == 'exit' or question == 'выход':
                print('До встречи!')
                break
            elif question in my_answers:
                print(my_answers[question])
            elif question in user_questions:
                print('Ты вроде уже спрашивал это')
            else:
                user_questions.append(question)
                print('У меня нет ответа на этот вопрос')
        else:
            print('Ты ничего не спросил')
    # print('user_questions =', user_questions)
    
if __name__ == "__main__":
    ask_user()
