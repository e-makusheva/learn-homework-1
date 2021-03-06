"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input('Введите возраст: '))
   
    def range_age(age):
        if age < 7:
            return 'иди в сад'
        elif 7 <= age < 17:
            return 'иди в школу'
        elif 17 <= age < 22:
            return 'иди в ВУЗ'
        else: 
            return 'работай'
    print (range_age(age))

if __name__ == "__main__":
    main()
