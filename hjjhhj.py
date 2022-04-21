a=6
b=5
pole=[    ['#','#','#','#','#','#','#','#','#','#'],
          ['#','*','*','*','*','*','*','*','w','#'],
          ['#','*','#','#','#','*','#','#','*','#'],
          ['#','*','w','*','*','*','*','*','*','#'],
          ['#','*','#','#','#','*','#','#','#','#'],
          ['#','*','#','*','*','*','*','*','*','#'],
          ['#','*','#','*','#','*','#','#','*','#'],
          ['#','*','#','*','#','#','#','#','*','#'],
          ['#','*','#','*','*','w','*','*','*','#'],
          ['#','M','#','#','#','#','#','#','#','#']] 
pole[a][b]='O'
for stroka in pole:
    for kletka in stroka:
        print(kletka,end='')
    print()
while True:
    k=input('Введите комманду:вверх,влево,вправо,вниз')
    if k=='вверх':
        pole[a][b]='*'
        a=a-1
        if a==-1:
            a=0
        elif pole[a][b]=='#':
            a=a+1
        elif pole[a][b]=='w':
            a=6
            b=5
        elif pole[a][b]=='M':
            break
        pole[a][b]='O'
    elif k=='влево':
        pole[a][b]='*'
        b=b-1
        if b==-1:
            b=0
        elif pole[a][b]=='#':
            b=b+1
        elif pole[a][b]=='w':
            a=6
            b=5
        elif pole[a][b]=='M':
            break
        pole[a][b]='O'
    elif k=='вниз':
        pole[a][b]='*'
        a=a+1
        if a==10:
            a=9
        elif pole[a][b]=='#':
            a=a-1
        elif pole[a][b]=='w':
            a=6
            b=5
        elif pole[a][b]=='M':
            break
        pole[a][b]='O'
    elif k=='вправо':
        pole[a][b]='*'
        b=b+1
        if b==10:
            b=9
        elif pole[a][b]=='#':
            b=b-1
        elif pole[a][b]=='w':
            a=6
            b=5
        elif pole[a][b]=='M':
            break
        pole[a][b]='O'
    for stroka in pole:
        for kletka in stroka:
            print(kletka,end='')
        print()