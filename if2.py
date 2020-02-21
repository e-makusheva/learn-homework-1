"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
  
  """
import sys
a=sys.argv[1]
b=sys.argv[2]
def check_string(a,b):
   if type(a) is not str or type(b) is not str:
     return 0
   elif a=='learn' and b=='learn':
     return '1 and 3'
   elif a==b:
     return 1
   elif len(a)>len(b) and b=='learn':
     return '2 and 3'
   elif len(a)>len(b):
     return 2
   elif b=='learn':
     return 3
   else:
     return ''
print(check_string(a,b))


                  


      
    
if __name__ == "__main__":
    main()
