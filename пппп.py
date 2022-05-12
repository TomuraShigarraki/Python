import random
def chislo():
    a=random.randint(1,9)
    b=random.randint(0,9)
    while b==a:
        b=random.randint(0,9)
    c=random.randint(0,9)
    while c==a or c==b:
        c=random.randint(0,9)
    return str(a)+str(b)+str(c)
def pobeda():
    if t==h
t=chislo()
'''
if a!=b and a!=c and b!=c:
    d=int(input('Введите первую цифру'))
    e=int(input('Введите вторую цифру'))
    f=int(input('Введите третью цифру'))
'''