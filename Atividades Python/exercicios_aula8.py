def exe1():
    numero = int(input('Digite um número inteiro: '))

    if numero >=1:
        print('Número Positivo')
    elif numero <=-1:
        print('Número Negativo')
    else:
        print('Valor igual a 0')

def exe2():
    idade = int(jnput('Digite sua idade: '))

    if idade >=16:
        print('Já pode votar')
    else:
        print('Ainda não pode votar')

def exe3():
    numero = int(input('Digite um número inteiro: '))

    if numero % 2 == 0:
        print('Número Par')
    else:
        print('Número ímpar')

def exe4():
    la = int(input('Digite um número inteiro: '))
    lb = int(input('Digite um número inteiro: '))
    lc = int(input('Digite um número inteiro: '))

    if la == lb == lc:
        print('Triângulo Equilátero')
    
    elif la == lb or la == lc or lc == lb:
        print('Triângulo Isósceles')
    
    else:
        print('Triangulo Escaleno')

def exe5():
    numero = int(input('Digite um número: '))

    if numero % 5 == 0 and numero % 7 == 0:
        print('Múltiplo de 5 e 7')
    
    else:
        print('Não é múltiplo de 5 e 7')

def exe6():
    numero = int(input('Digite um número: '))

    if numero >= 10:
        print('Número positivo maior ou igual a 10')
    elif numero < 10 and numero > 0:
        print('Número menor que 10, mas positivo')
    elif numero == 0:
        print('Número igual a 0')
    else:
        print('Número negativo e menor que 10')

def exe7():
    numero = int(input('Digite um número: '))

    if numero % 3 == 0 and numero % 5 == 0:
        print('Número é divisível por 3 e 5')
    else:
        print('Número não é divisível por 3 e 5')
    