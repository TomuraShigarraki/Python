dela=['убраться','пропылесосить','покормить животных']
command=''
while command!='стоп':
    command=input('Введите команду').lower()
    if command=='добавить':
        a=input('Добавьте дело в список')
        dela.append(a)
    elif command=='удалить':
        b=input('Введите дело из списка для удаления')
        dela.remove(b)
    elif command=='показать элемент по номеру':
        c=int(input('Введите номер дела'))
        print(dela[c])
    elif command=='показать весь список':
        print(dela)
    elif command=='редактировать':
        d=int(input('Введите номер дела'))
        f=input('Введите на что хотите заменить')
        dela.remove(dela[d])
        dela.insert(d,f)