import pyautogui
import time
import random
a=0
b=0
command=''
print('Чтобы ознакомиться со списком комманд введите "помощь"')
while(command!='стоп'):
    command=input('Введите команду').lower()
    if command=='помощь':
            print('Вот список команд: Стоп, Сумма, Умножение, Деление, Разность, Быстрое закрытие, Поиск, Рандомайзер,Квадрат')
    elif command=='сумма':
            a=int(input('Введите первое число'))
            b=int(input('Введите второе число'))
            print(a+b)
    elif command=='разность':
            a=int(input('Введите первое число'))
            b=int(input('Введите второе число'))
            print(a-b)
    elif command=='умножение':
            a=int(input('Введите первое число'))
            b=int(input('Введите второе число'))
            print(a*b)
    elif command=='деление':
            a=int(input('Введите первое число'))
            b=int(input('Введите второе число'))
            print(a/b)
    elif command=='быстрое закрытие':
            pyautogui.hotkey('alt', 'f4')
    elif command=='поиск':
            c=input('Введите запрос')
            pyautogui.moveTo(242,1044)
            pyautogui.click()
            time.sleep(10)
            pyautogui.write(c)
            time.sleep(10)
            pyautogui.press('enter')
    elif command=='рандомайзер':
            d=int(input('Введите масимальное число'))
            f=random.randint(0,d)
            print(f)
    elif command=='квадрат':
            for i in range(1,7):
                print('******')