pole=[['*','*','*','*','*','*','*','*','*','*'],
        ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*'],
          ['*','*','*','*','*','*','*','*','*','*']] 
while True:
    a=int(input('Введите номер строки'))-1
    b=int(input('Введите номер столбца'))-1
    if (a>9 or b>9) or (a<0 or b<0):
        print('места нет')
    else:
        break
pole[a][b]='O'
for stroka in pole:
    for kletka in stroka:
        print(kletka,end='')
    print()