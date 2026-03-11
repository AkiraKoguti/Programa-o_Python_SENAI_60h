import random

print('============')
print('Mega Sena!!!')
print('============')

num_mega = list(range(1,61))

quant_num_aposta = int(input('A partir de 6: '))

if quant_num_aposta == 6:
    n1 = random.choice(num_mega)
    n2 = random.choice(num_mega)
    n3 = random.choice(num_mega)
    n4 = random.choice(num_mega)
    n5 = random.choice(num_mega)
    n6 = random.choice(num_mega)
    lista_maq = [n1,n2,n3,n4,n5,n6]

    print(lista_maq)
    m1 = int(input('Escolha de 1 a 60: '))
    m2 = int(input('Escolha de 1 a 60: '))
    m3 = int(input('Escolha de 1 a 60: '))
    m4 = int(input('Escolha de 1 a 60: '))
    m5 = int(input('Escolha de 1 a 60: '))
    m6 = int(input('Escolha de 1 a 60: '))
    print()
    
    minha_lista = []

    if m1 in lista_maq:
        minha_lista.append(m1)
        if m2 in lista_maq:
            minha_lista.append(m2)
            if m3 in lista_maq:
                minha_lista.append(m3) 
                if m4 in lista_maq:
                    minha_lista.append(m4)
                    if m5 in lista_maq:
                        minha_lista.append(m5)
                        if m6 in lista_maq:
                            minha_lista.append(m6)
  
    tamanho_meu = len(minha_lista)
    
    if tamanho_meu == 6:
        print('==========================')
        print('Você ganho na MEGA SENA!!!')
        print('==========================')
        print(minha_lista), print(lista_maq)
    elif tamanho_meu == 5:
        print('=========================')
        print('Você acertou uma Quina!!!')
        print('=========================')
        print(minha_lista), print(lista_maq)
    elif tamanho_meu == 4:
        print('==========================')
        print('Você acertou uma Quadra!!!')
        print('==========================')
        print(minha_lista), print(lista_maq)
    else:
        print('Que pena, você não conseguiu...' \
        'mais sorte da próxima vez')
        print(minha_lista), print(lista_maq)

    print('Quantidade de acertos ->', tamanho_meu)
