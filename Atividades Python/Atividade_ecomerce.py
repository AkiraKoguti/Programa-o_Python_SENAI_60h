# Produtos E-Comerce

ecomerce = {
'Livros' : ['', '1 - Livro1','2 - Livro2','3 - Livro3'],
'Tablets' : ['', 'Marca1', 'Marca2', 'Marca3'],
'Fones' : ['', 'Fone', 'Fone2', 'Fone3']
}

# Preços E-Comerce

ecomercepreco = {
'Livros' : [0, 40.00, 129.99, 17.89],
'Tablets' : [0, 899.99,500.00, 4599.99],
'Fones' : [0, 250.00, 59.99, 119.99]
}

# Interface E-Comerce

print('Seja bem vindo ao E-Comerce Y')

print('Livros|Tablets|Fones')
sessao = input('Selecione uma das sessões: ')
print(ecomerce[sessao])
carrinho1 = int(input('Selecione qual item deseja comprar: '))
preco1 = ecomercepreco[sessao][carrinho1]
print()

print('Livros|Tablets|Fones')
sessao = input('Selecione uma das sessões: ')
print(ecomerce[sessao])
carrinho2 = int(input('Selecione qual item deseja comprar: '))
preco2 = ecomercepreco[sessao][carrinho2]
print()

print('Livros|Tablets|Fones')
sessao = input('Selecione uma das sessões: ')
print(ecomerce[sessao])
carrinho3 = int(input('Selecione qual item deseja comprar: '))
preco3 = ecomercepreco[sessao][carrinho3]
print()

# Final/Pagamento E-Comerce
precototal = preco1+preco2+preco3
print('Preço total = ', precototal)
