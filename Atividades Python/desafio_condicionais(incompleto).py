dados_clientes = {

'nomes':[],
'idades':[],
'dias':[],
'quartos':[]
}

# Cadastro hospede 1
cadastro1 = dados_clientes['nomes'].append(input('Digite seu nome: ')),  dados_clientes['idades'].append(input('Digite sua idade: ')), dados_clientes['dias'].append(int(input('Tempo de estadia: ')))
print('''
Escolha um quarto

1 - Simples | 2 - Duplo | 3 - Luxo ''')

escolha_quarto1 = dados_clientes['quartos'].append(int(input('-> ')))





# Pagamento hospede 1
if dados_clientes['quartos'][0] == 1:
    preco1 = 100 * dados_clientes['dias'][0]
elif dados_clientes['quartos'][0] == 2:
    preco1 = 150 * dados_clientes['dias'][0]
elif dados_clientes['quartos'][0] == 3:
    preco1 = 250 * dados_clientes['dias'][0]

    


























# cadastro2 = dados_clientes['nomes'].append(input('Digite seu nome: ')),  dados_clientes['idades'].append(input('Digite sua idade: '))


# cadastro3 = dados_clientes['nomes'].append(input('Digite seu nome: ')),  dados_clientes['idades'].append(input('Digite sua idade: '))
