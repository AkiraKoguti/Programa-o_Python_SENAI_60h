def exer1():
    # Exercício 1
    try:
        a = int(input('Digite o 1° número inteiro: '))
        b = int(input('Digite o 2° número inteiro: '))
        print(a+b)
    except ValueError:
        print('Digite apenas número inteiros')

def exer2():
    # Exercício 2
    try:
        a = float(input('Digite o 1° número: '))
        b = float(input('Digite o 2° número: '))
        print(a/b)
    except ZeroDivisionError:
        print('Erro... Número não pode ser igual a zero(0)')

def exer3():
    # Exercício 3
    l = ['slot 0','slot 1','slot 2']
    try:
        esc = int(input('Escolha um slot da lista de 0 a 2: '))
        print(l[esc])
    except IndexError:
        print('Escolha um número de slot entre 0 e 2')
