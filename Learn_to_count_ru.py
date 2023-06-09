# Импортируем random
import random

# Функция для проверки правильности вводимой цифры
def number_control(num):
    # Проверить до тех пор пока не будет введен слово stop или число
    while True:
        if num == 'stop':
            break
        elif not num.isdigit():
            num = input('Ваш ответ: ')
        else:
            break
    return num


# Знакомства с игрой
print('Компютер составляет пример. Введите ответ.')
print('Для завершения работы введите "stop"')
print('*'*50)


# Подсчет очков
point = 0
# Подсчет игр
task_processing = 0
# Подсчет правильных ответов
correct_answer = 0
# Подсчет неправильных ответов
incorrect_answer = 0
# Провент верных ответов
percentage = 0

# Главный цикл
user = ''
while user != 'stop':
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    argument = ['-','+','*']
    argument_choice = random.choice(argument)

    # Условия, если первое случайное число будет меньше второго, тогда поменять местами
    if number1 < number2:
        number1, number2 = number2, number1

    # Если резултат деление будет бесконечно длинное вещественное число,тогда найти подходящий ответ до тех пор пока оно не будет найдено
    if argument_choice == '/':
        for i in range(100):
            number_sum = eval(str(number1) + argument_choice + str(number2))
            if number_sum - int(number_sum) == 0.0:
                print(f"{number1} {argument_choice} {number2} = {int(number_sum)}")
                break
            else:
                number1 = random.randint(1, 100)
                number2 = random.randint(1, 100)

    # Перемення для подсчета суммы двух случайных цифр и случайного арифметического оператора
    number_sum = eval(str(number1) + argument_choice + str(number2))

    # Резултаты пользователя
    print(f'Ваши очки: {point}')
    print(f'Обработано задач: {task_processing}')
    print(f'Правильных ответов: {correct_answer}')
    print('-' * 40)

    # Переменная user запращивает цифру от пользователя и проверяет вводимые данные
    print(f"{number1} {argument_choice} {number2} = ")
    user = input('Ваш ответ: ')
    user = number_control(user)

    # условия если пользователь ввел слово stop или у него закончатся очки, тогда игра заканчивается
    if user == 'stop':
        break
    elif point < 0:
        print('У вас закончились очки')
        break
    user = int(user)


    # Переменная для посчтета игр
    task_processing += 1

    # Условия если ответ будет правильным
    if user == number_sum:
        point += 10
        correct_answer += 1
        print('')
        print('Правильно!')
        print('')

    # Условия если ответ будет неправильным
    elif user != number_sum:
        point -= 5
        incorrect_answer += 1
        print('')
        print(f'Ответ неправильный... Правильно: {number_sum}')
        print('')

# Содержание и результаты игры
print('*'*50)
print('СТАТИСТИКА ИГРЫ')
print(f'Всего примеров: {task_processing}')
print(f'Правильных ответов: {correct_answer}')
print(f'Неправильных ответов: {incorrect_answer}')
print(f'Процент верных ответов: {int((correct_answer/task_processing)*100)}%')
print(f'Возвращайтесь!')
