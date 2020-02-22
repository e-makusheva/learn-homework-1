"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    school_scores = [
      {'school_class': '4a', 'scores': [3,4,4,5,2]},
      {'school_class': '8b', 'scores': [3,5,2,5,2]},
      {'school_class': '11a', 'scores': [3,4,5,5,5]}
    ]    
    sum_school = 0
    cnt_school = 0
        
    for common_result in school_scores:
        for mark1 in common_result['scores']:
            sum_school += mark1
        cnt_school += len(common_result['scores'])
    print(f'средняя оценка в школе = {sum_school / cnt_school}')

    print("=======")

    for class_result in school_scores:
        sum_class = 0
        cnt_class = 0
        for mark2 in class_result['scores']:
            sum_class += mark2
        cnt_class = len(class_result['scores'])
        print(f"средняя оценка класса {class_result['school_class']} = {sum_class/cnt_class}")

        

if __name__ == "__main__":
    main()
