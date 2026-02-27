print('''
===================
Sistema Média Aluno
===================
''')

nome = input('Digite o nome do aluno: ')
print()

print('Digite as notas do aluno:', nome)
n1 = float(input('Nota1 '))
n2 = float(input('Nota2 '))
n3 = float(input('Nota3 '))
print('''
===========
Média Aluno
===========
''')

media = (n1+n2+n3)/3

print('Média do aluno(a)', nome)
print(round(media,2))

aprovado = media>=7
recuperacao = media<7 and media>=5
reprovado = media<5

print(f'''
========================
Situação Aluno(a) {nome}
========================

Aprovado(a)? {aprovado}
Recuperação? {recuperacao}
Reprovado(a)? {reprovado}
''')
