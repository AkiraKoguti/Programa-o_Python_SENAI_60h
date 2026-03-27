import os
import shutil


# Exercício 1
# with open('testes.txt','w') as arquivo:
#     arquivo.write('Teste Teste Teste')

# with open('testes.txt', 'r') as arquivo:
#     conteúdo = arquivo.read()
#     print(conteúdo)

# Exercício 2
# os.mkdir('Novo_diretorio')

# Exercício 3
# os.rename('Novo_diretorio','diretorio1')

# Exercício 4
with os.scandir('diretorio2') as entrada:
    for arquivo in entrada:
        if arquivo.is_file():
            print(f'arquivo encontrado: {arquivo.name}')

# Exercício 5
import shutil
shutil.copytree('diretorio2', 'diretorio2.5')

# Exercício 6
import shutil
shutil.rmtree('diretorio2.5')