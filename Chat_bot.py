import pyautogui,time#
a=0
b=0
command=''
while(command!='Стоп'):
    command=input('Введите команду')
    if command=='Помощь':
            print('Вот список команд: Стоп, Сумма, Умножение, Деление, Разность, Быстрое закрытие, Поиск')
    elif command=='Сумма':
            a=int(input('Введите первое число'))
            b=int(input('Введите второе число'))
            print(a+b)
    elif command=='Разность':
            a=int(input('Введите первое число'))
            b=int(input('Введите второе число'))
            print(a-b)
    elif command=='Умножение':
            a=int(input('Введите первое число'))
            b=int(input('Введите второе число'))
            print(a*b)
    elif command=='Деление':
            a=int(input('Введите первое число'))
            b=int(input('Введите второе число'))
            print(a/b)
    elif command=='Быстрое закрытие':
            pyautogui.hotkey('alt', 'f4')
    elif command=='Поиск':
            c=input('Введите запрос')
            pyautogui.moveTo(242,1044)
            pyautogui.click()
            time.sleep(10)
            pyautogui.write(c)
            time.sleep(10)
            pyautogui.press('enter')
    elif command==