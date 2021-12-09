command=input('Введите команду')
while(command!='Стоп'):
    command=input('Введите команду')
    if command=='Помощь':
        print('Вот список команд: Стоп, Сумма, Умножение, Деление, Разность)
    elif command=='Сумма':
        a=int(input('Введите первое число')