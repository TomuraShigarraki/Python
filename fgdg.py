dela=['убраться','пропылесосить','покормить животных']
command=''
while(command!='стоп')
    command=input('Введите команду').lower()
    if command='добавить':
        a=input('Добавьте дело в список')
        dela.append(a)
    elif command='удалить':
        b=input('Введите дело из списка для удаления')
        dela.remove(b)
