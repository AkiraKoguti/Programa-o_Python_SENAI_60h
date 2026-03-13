dados_escola = {

'dados_alunos':{
    'nomes_alunos':['Pedro', 'Fernando', 'Gustavo', 'Paulo'],
    'notas_alunos':[[5,],[5,],[5,],[5,]]
},

'dados_professor':{
    'nome':'Fábio',
    'senha':'1234'
}

}

for tentativas in range(3):
    print('Site Escola Estadual X')
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    print()


    

    if nome == dados_escola['dados_professor']['nome'] and senha == dados_escola['dados_professor']['senha']:
        menu = input('Deseja ir ao menu? sim - ir | não - sair\n-> ')
        while menu == 'sim' or menu == 'Sim' or menu == 's':
            print('Seja bem vindo(a) professor(a)')
            print('O que deseja fazer:\n1 - Inserir notas | 2 - Ver médias')
            escolha = int(input('-> '))
            
            if escolha == 1:
                print('Alunos: Pedro | Fernando | Gustavo | Paulo')
                print('Qual aluno deseja adicionar nota?')
                escolher_aluno = input('Digite o nome: ')
                id_aluno = dados_escola['dados_alunos']['nomes_alunos'].index(escolher_aluno)

                print('Quantas notas deseja adicionar?')
                q_notas = int(input('Digite a quantidade: '))


                for quantidade in range(q_notas):
                    nota_add = int(input('Digite a nota: '))
                    dados_escola['dados_alunos']['notas_alunos'][id_aluno].append(nota_add)
                else:
                    menu = input('Deseja ir ao menu? sim - ir | não - sair\n-> ')

            elif escolha == 2:
                print(f'''
============
Média alunos
============
_______________
Aluno 1

Nome: {dados_escola['dados_alunos']['nomes_alunos'][0]}
Média: {round(sum(dados_escola["dados_alunos"]['notas_alunos'][0]) / len(dados_escola["dados_alunos"]['notas_alunos'][0]),2)}
_______________
Aluno 2

Nome: {dados_escola['dados_alunos']['nomes_alunos'][1]}
Média: {round(sum(dados_escola["dados_alunos"]['notas_alunos'][1]) / len(dados_escola["dados_alunos"]['notas_alunos'][1]),2)}
_______________
Aluno 3

Nome: {dados_escola['dados_alunos']['nomes_alunos'][2]}
Média: {round(sum(dados_escola["dados_alunos"]['notas_alunos'][2]) / len(dados_escola["dados_alunos"]['notas_alunos'][2]),2)}
_______________
Aluno 4

Nome: {dados_escola['dados_alunos']['nomes_alunos'][3]}
Média: {round(sum(dados_escola["dados_alunos"]['notas_alunos'][3]) / len(dados_escola["dados_alunos"]['notas_alunos'][3]),2)}

''')

        else:
            print('Até mais')
            break

else:
    print('Nome ou senha incorreta, tente novamente mais tarde.')
a = input('Digite enter para sair\n-> ')