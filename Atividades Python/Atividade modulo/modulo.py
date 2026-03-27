import random

def atv1():
    return random.randint(5,10)

def atv2():
    x = random.randint(1,10)
    y = random.randint(1,10)
    z = random.randint(1,10)
    return x,y,z

def atv3():
    return random.randrange(10,30)

def atv4():
    a = 11
    for x in range(10):
        a = a-1
        print(a)
    return 'Fogo!'

def atv5():
    l = []
    num_int = int(input('Insira um número: '))
    for x in range(1,num_int):
        if x % 2 == 0:
            l.append(x)
    print(l)
    som = sum(l)
    return som

def atv6():
    n_taboada = int(input('Escolha um número para a taboada: '))
    for x in range(1,11):
        val = n_taboada*x
        print(n_taboada,'x',x,'=',val)

def atv7():
    a = 99
    for x in range(1,100):
        if a % 2 != 0:
            print(a)
        a = a-1
atv7()