import tkinter as tk

def enviar():
    print(nome(),idade(),email(),endereco(),cell(),cep(),cidade(),cursos())

def nome():
    dado = input_nome.get()
    return'Nome:', dado

def idade():
    dado = input_idade.get()
    return'Idade:', dado

def email():
    dado = input_email.get()
    return'Email:', dado

def endereco():
    dado = input_endereco.get()
    return'Endereço:',dado

def cell():
    dado = input_cell.get()
    return'Cell:',dado

def cep():
    dado = input_cep.get()
    return'CEP:',dado

def cidade():
    dado = input_cidade.get()
    return'Cidade:',dado

def cursos():
    dado = input_cursos.get()
    return'Cursos:',dado



janela = tk.Tk()
janela.geometry('800x900')
janela.configure(bg = 'white')

# Texto Cadastro
tk.Label(janela, text = 'Cadastro', font=('arial', 25), bg = 'white').pack(pady=45)

# Texto e input Nome:
tk.Label(janela, text=('Nome'), font=('arial', 15), bg = 'white').pack()
input_nome = tk.Entry(janela, font=('arial', 20), bg = 'white')
input_nome.pack()

# Texto e input Idade:
tk.Label(janela, text=('Idade'), font=('arial', 15), bg = 'white').pack()
input_idade = tk.Entry(janela, font=('arial', 20), bg = 'white')
input_idade.pack()

# Texto e input E-Mail:
tk.Label(janela, text=('E-mail'), font=('arial', 15), bg = 'white').pack()
input_email = tk.Entry(janela, font=('arial', 20), bg = 'white')
input_email.pack()

# Texto e input Endereço:
tk.Label(janela, text=('Endereço'), font=('arial', 15), bg = 'white').pack()
input_endereco = tk.Entry(janela, font=('arial', 20), bg = 'white')
input_endereco.pack()

# Texto e input Num Cell:
tk.Label(janela, text=('Celular'), font=('arial', 15), bg = 'white').pack()
input_cell = tk.Entry(janela, font=('arial', 20), bg = 'white')
input_cell.pack()

# Texto e input CEP:
tk.Label(janela, text=('CEP'), font=('arial', 15), bg = 'white').pack()
input_cep = tk.Entry(janela, font=('arial', 20), bg = 'white')
input_cep.pack()

# Texto e input Cidade:
tk.Label(janela, text=('Cidade'), font=('arial', 15), bg = 'white').pack()
input_cidade = tk.Entry(janela, font=('arial', 20), bg = 'white')
input_cidade.pack()

# Texto e input Cursos:
tk.Label(janela, text=('Cursos'), font=('arial', 15), bg = 'white').pack()
input_cursos = tk.Entry(janela, font=('arial', 20), bg = 'white')
input_cursos.pack()

# Botão enviar:
btn_env = tk.Button(janela, text= 'Enviar', font=('arial', 15), bg = 'white', command=enviar)
btn_env.pack(pady=40)


janela.mainloop()