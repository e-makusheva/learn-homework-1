"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    """
    Замените pass на ваш код
      """

dialog = {'как дела?': 'хорошо', 'что делаешь?': 'программирую'}
while True:
    try:
        user_question = input('пользователь: ')
        if user_question in dialog:
            print(f'программа: {dialog[user_question]}')
    except KeyboardInterrupt:
        print('')
        print('программа: пока!')
        break
    
if __name__ == "__main__":
    ask_user()
