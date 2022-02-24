slovo='privet'
slovo.split()
otvet=[]
while otvet!=slovo:
    bukva=input('Введите букву')
    if bukva=='p':
        print('правильно')
        otvet.insert(0,'p')
    elif bukva=='r':
        print('правильно')
        otvet.insert(1,'r')
    elif bukva=='i':
        print('правильно')
        otvet.insert(2,'i')
    elif bukva=='v':
        print('правильно')
        otvet.insert(3,'v')
    elif bukva=='e':
        print('правильно')
        otvet.insert(4,'e')
    elif buvka=='t':
        print('правильно')
        otvet.insert(5,'t')
    else