# Produtos E-Comerce

ecomerce = {
'Livros' : ['', '1 - Livro1','2 - Livro2','3 - Livro3'],
'Tablets' : ['', 'Marca1', 'Marca2', 'Marca3'],
'Fones' : ['', 'Fone', 'Fone2', 'Fone3']
}

# Preços E-Comerce

ecomercepreco = {
'Livros$' : [0, 40.00, 129.99, 17.89],
'Tablets$' : [0, 899.99,500.00, 4599.99],
'Fones$' : [0, 250.00, 59.99, 119.99]
}

# Interface E-Comerce

print('Seja bem vindo ao E-Comerce Y')

print(ecomerce['Livros'])
carrinholv = int(input('Selecione qual livro deseja comprar: '))
precolv = ecomercepreco['Livros$'][carrinholv]
print('livro selecionado =', ecomerce['Livros'][carrinholv])
print()

print(ecomerce['Tablets'])
carrinhotab = int(input('Selecione qual Tablet deseja comprar: '))
precotab = ecomercepreco['Tablets$'][carrinhotab]
print('livro selecionado =', ecomerce['Tablets'][carrinhotab])
print()

print(ecomerce['Fones'])
carrinhofone = int(input('Selecione qual fone deseja comprar: '))
precofone = ecomercepreco['Fones$'][carrinhofone]
print('livro selecionado =', ecomerce['Fones'][carrinhofone])
print()

# Final/Pagamento E-Comerce

precototal = precolv+precotab+precofone
print('Preço total = ', precototal)