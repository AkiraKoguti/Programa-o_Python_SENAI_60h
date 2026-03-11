dados_clientes = {

'nomes':[],
'idades':[],
'dias':[],
'quartos':[]
}

# Cadastro Hóspede 1
print('Hóspede N°1')
cadastro1 = dados_clientes['nomes'].append(input('Digite seu nome: ')),  dados_clientes['idades'].append(input('Digite sua idade: ')), dados_clientes['dias'].append(int(input('Tempo de estadia: ')))
print('''
Escolha um quarto

1 - Simples | 2 - Duplo | 3 - Luxo ''')

escolha_quarto1 = dados_clientes['quartos'].append(int(input('-> ')))
print()


# Cadastro Hóspede 2
print('Hóspede N°2')
cadastro2 = dados_clientes['nomes'].append(input('Digite seu nome: ')),  dados_clientes['idades'].append(input('Digite sua idade: ')), dados_clientes['dias'].append(int(input('Tempo de estadia: ')))
print('''
Escolha um quarto

1 - Simples | 2 - Duplo | 3 - Luxo ''')

escolha_quarto2 = dados_clientes['quartos'].append(int(input('-> ')))
print()


# Cadastro Hóspede 3
print('Hóspede N°3')
cadastro3 = dados_clientes['nomes'].append(input('Digite seu nome: ')),  dados_clientes['idades'].append(input('Digite sua idade: ')), dados_clientes['dias'].append(int(input('Tempo de estadia: ')))
print('''
Escolha um quarto

1 - Simples | 2 - Duplo | 3 - Luxo ''')

escolha_quarto3 = dados_clientes['quartos'].append(int(input('-> ')))




# Pagamento Hóspede 1
if dados_clientes['quartos'][0] == 1:
    preco1 = 100 * dados_clientes['dias'][0]
elif dados_clientes['quartos'][0] == 2:
    preco1 = 150 * dados_clientes['dias'][0]
elif dados_clientes['quartos'][0] == 3:
    preco1 = 250 * dados_clientes['dias'][0]


# Pagamento Hóspede 2
if dados_clientes['quartos'][1] == 1:
    preco2 = 100 * dados_clientes['dias'][1]
elif dados_clientes['quartos'][1] == 2:
    preco2 = 150 * dados_clientes['dias'][1]
elif dados_clientes['quartos'][1] == 3:
    preco2 = 250 * dados_clientes['dias'][1]


# Pagamento Hóspede 3
if dados_clientes['quartos'][2] == 1:
    preco3 = 100 * dados_clientes['dias'][2]
elif dados_clientes['quartos'][2] == 2:
    preco3 = 150 * dados_clientes['dias'][2]
elif dados_clientes['quartos'][2] == 3:
    preco3 = 250 * dados_clientes['dias'][2]


# Recibo

print(f'''

-====================-
Pagamento dos Hospedes
-====================-
      
Hóspede N°1

Nome: {dados_clientes["nomes"][0]}
Idade: {dados_clientes["idades"][0]}
Valor Hospedagem: {preco1}
______________________

Hóspede N°2

Nome: {dados_clientes["nomes"][1]}
Idade: {dados_clientes["idades"][1]}
Valor Hospedagem: {preco2}
______________________

Hóspede N°3

Nome: {dados_clientes["nomes"][2]}
Idade: {dados_clientes["idades"][2]}
Valor Hospedagem: {preco3}
''')

    
















