from conexao import connect
from bd import insert, update, delete, query, register, login, to_lend, give_back
from livro import Livro
from datetime import datetime
from usuario import Usuario
from tkinter import * 
import tkinter as tk
from conexao import connect

tk.Tk()
mydb = connect()

# Conectar ao banco de dados
mydb = connect()

print("Bem-vindo à Biblioteca")

while True:
    print("\nSelecione a operação desejada:")
    print("1. Registrar usuário")
    print("2. Fazer login")
    print("3. Inserir livro")
    print("4. Atualizar livro")
    print("5. Excluir livro")
    print("6. Consultar livros")
    print("7. Emprestar livro")
    print("8. Devolver livro")
    print("9. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input('Digite o Nome: ')
        email = input('Digite o Email: ')
        senha = input('Digite a Senha: ')
        data_nascimento = input('Digite a Data de Nascimento (DD/MM/YYYY): ')
        # Converter a string de data para um objeto datetime
        data_nascimento_obj = datetime.strptime(data_nascimento, '%d/%m/%Y')
        # Formatar a data no formato MySQL
        data_nascimento_formatada = data_nascimento_obj.strftime('%Y-%m-%d')
        rua = input('Digite a Rua: ')
        bairro = input('Digite o Bairro: ')
        cidade = input('Digite a Cidade: ')
        estado = input('Digite o Estado: ')
        cep = input('Digite o CEP: ')
        
        user = Usuario(nome, email, senha, data_nascimento, rua, bairro, cidade, estado, cep)

        register(mydb, user.nome, user.email, user.senha, user.data_nascimento,
                 user.rua, user.bairro, user.cidade, user.estado, user.cep)

    elif opcao == "2":
        email = input('Digite o Email: ')
        senha = input('Digite a Senha: ')

        user = login(mydb, email, senha)

    elif opcao == "3":
        titulo = input('Digite o Título: ')
        autor = input('Digite o Autor: ')
        ano = input('Digite o Ano: ')
        status_ = input(
            'Digite o Status (1 para Disponível, 0 para Indisponível): ')

        l = Livro(titulo, autor, ano)
        insert(mydb, l.titulo, l.autor, l.ano, status_)

    elif opcao == "4":
        titulo_antigo = input(
            'Digite o título do livro que deseja atualizar: ')
        titulo_novo = input('Digite o novo título: ')
        autor = input('Digite o novo autor: ')
        ano = input('Digite o novo ano: ')
        status_ = input(
            'Digite o novo status (1 para Disponível, 0 para Indisponível): ')

        update(mydb, titulo_antigo, titulo_novo, autor, ano, status_)

    elif opcao == "5":
        titulo = input('Digite o título do livro que deseja excluir: ')
        delete(mydb, titulo)

    elif opcao == "6":
        query(mydb)

    elif opcao == "7":
        if 'user' not in locals():
            print("Você precisa fazer login para emprestar um livro.")
            continue

        titulo = input('Digite o título do livro que deseja emprestar: ')
        to_lend(mydb, user, titulo)
    elif opcao == "8":
        if 'user' not in locals():
            print("Você precisa fazer login para devolver um livro.")
            continue

        titulo = input('Digite o título do livro que deseja devolver: ')
        give_back(mydb, user, titulo)


    elif opcao == "9":
        break

    else:
        print("Opção inválida!")

# Fechar a conexão com o banco de dados
mydb.close()

def register_livro():
    
    janela2 = tk.Toplevel()
    janela2.title("Página do Cadastro")

    text_cadastro = tk.Label(janela2, text="Cadastro do usuário!")
    text_cadastro.grid(column=0, row=2, padx= 10, pady=10)

    text_nome = tk.Label(janela2, text="Digite seu nome")
    text_nome.grid(column=0, row=3, padx=10, pady=10)
    E1 = tk.Entry(janela2)
    E1.grid(column=0, row=4, padx=10, pady=10)

    text_email = tk.Label(janela2,text= "Digite seu email")
    text_email.grid(column=0,row=5, padx=10, pady=10)
    E2 = tk.Entry(janela2)
    E2.grid(column=0, row=6, padx= 10, pady=10)

    text_senha = tk.Label(janela2,text= "Digite sua senha")
    text_senha.grid(column=0,row=7, padx=10, pady=10)
    E3 = tk.Entry(janela2)
    E3.grid(column=0, row=8, padx=10, pady=10)

    text_data_nasc = tk.Label(janela2,text= "Digite sua data de nascimento")
    text_data_nasc.grid(column=0,row=9, padx=10, pady=10)
    E4 = tk.Entry(janela2)
    E4.grid(column=0, row=10, padx=10, pady=10)

    text_rua = tk.Label(janela2,text= "Digite sua rua")
    text_rua.grid(column=0,row=11, padx=10, pady=10)
    E5 = tk.Entry(janela2)
    E5.grid(column=0, row=12, padx=10, pady=10)

    text_bairro= tk.Label(janela2,text= "Digite seu bairro")
    text_bairro.grid(column=1,row=3, padx=10, pady=10)
    E6 = tk.Entry(janela2)
    E6.grid(column=1, row=4, padx=10, pady=10)

    text_cidade = tk.Label(janela2,text= "Digite sua cidade")
    text_cidade.grid(column=1,row=5, padx=10, pady=10)
    E7 = tk.Entry(janela2)
    E7.grid(column=1, row=6, padx=10, pady=10)

    text_estado = tk.Label(janela2,text= "Digite seu estado")
    text_estado.grid(column=1,row=7, padx=10, pady=10)
    E8 = tk.Entry(janela2)
    E8.grid(column=1, row=8, padx=10, pady=10)

    text_cep = tk.Label(janela2,text= "Digite seu cep")
    text_cep.grid(column=1,row=9, padx=10, pady=10)
    E9 = tk.Entry(janela2)
    E9.grid(column=1, row=10, padx=10, pady=10)
    
    nome = E1.get()
    email = E2.get()
    senha = E3.get()
    data_nascimento = E4.get()
    rua = E5.get()
    bairro = E6.get()
    cidade = E7.get()
    estado = E8.get()
    cep = E9.get()

    logando = register(mydb,nome, email, senha, data_nascimento, rua, bairro, cidade, estado, cep)

    botao_voltar1 = tk.Button(janela2, text="Fechar a janela", command= janela2.destroy)
    botao_voltar1.grid(column=0, row=1, padx=10, pady=10)

    botao_entrar1 = tk.Button(janela2, text="Entrar", command=livros)
    botao_entrar1.grid(column=0, row=15,  padx= 10, pady=10)

def login_livro():
    janela3 = tk.Toplevel()
    janela3.title("Página do Login")
    
    text_login = tk.Label(janela3, text="Login do usuário!")
    text_login.grid(column=0, row=1, padx= 10, pady=10)

    text_email = tk.Label(janela3,text= "Digite seu email")
    text_email.grid(column=0,row=2, padx= 10, pady=10)
    E1 = tk.Entry(janela3)
    E1.grid(column=0, row=3, padx= 10, pady=10)

    text_senha = tk.Label(janela3,text= "Digite sua senha")
    text_senha.grid(column=0,row=4, padx= 10, pady=10)
    E2 = tk.Entry(janela3)
    E2.grid(column=0, row=5, padx= 10, pady=10)

    email = E1.get()
    senha = E2.get()

    logando = login(mydb, email, senha)

    botao_voltar2 = tk.Button(janela3, text="Fechar a janela", command= janela3.destroy)
    botao_voltar2.grid(column=0, row=1,  padx= 10, pady=10)

    botao_entrar2 = tk.Button(janela3, text="Entrar", command=livros)
    botao_entrar2.grid(column=0, row=7,  padx= 10, pady=10)

def livros():
    janela7 = tk.Toplevel()
    janela7.title("Livros")
    
    text_livro = tk.Label(janela7, text="Selecione a opção desejada:")
    text_livro.grid(column=0, row=2, padx= 10, pady=10)

    texto_orientacao4 = Label(janela7, text="Clique no botão para fazer o cadastro do livro: ")
    texto_orientacao4.grid(column=0, row=3, padx= 10, pady=10)
    botao1 = tk.Button(janela7, text="Clique aqui", command=cadastro_livros)
    botao1.grid(column=0, row=4, padx= 10, pady=10)

    texto_orientacao5 = Label(janela7, text="Clique no botão para fazer a atualizção um livro: ")
    texto_orientacao5.grid(column=0, row=5, padx= 10, pady=10)
    botao2 = tk.Button(janela7, text="Clique aqui", command=atualizar_livros)
    botao2.grid(column=0, row=6, padx= 10, pady=10)

    texto_orientacao7 = Label(janela7, text="Clique no botão para emprestar um livro: ")
    texto_orientacao7.grid(column=0, row=9, padx= 10, pady=10)
    botao3 = tk.Button(janela7, text="Clique aqui", command=emprestar_livros)
    botao3.grid(column=0, row=10, padx= 10, pady=10)

    texto_orientacao8 = Label(janela7, text="Clique no botão para devolver um livro: ")
    texto_orientacao8.grid(column=0, row=11, padx= 10, pady=10)
    botao4 = tk.Button(janela7, text="Clique aqui", command=devolver_livros)
    botao4.grid(column=0, row=12, padx= 10, pady=10)

    texto_orientacao9 = Label(janela7, text="Clique no botão para visualizar os livro: ")
    texto_orientacao9.grid(column=0, row=13, padx= 10, pady=10)
    botao5 = tk.Button(janela7, text="Clique aqui", command=listar_livros)
    botao5.grid(column=0, row=14, padx= 10, pady=10)

    botao_voltar3 = tk.Button(janela7, text="Fechar a janela", command= janela7.destroy)
    botao_voltar3.grid(column=0, row=1, padx=10, pady=10)

def cadastro_livros():
    janela4 = tk.Toplevel()
    janela4.title("Página do cadastro de livros")
    
    text_cadastro = tk.Label(janela4, text="Cadastrar um livro!")
    text_cadastro.grid(column=0, row=2, padx= 10, pady=10)

    text_titulo = tk.Label(janela4,text= "Digite o título do livro:")
    text_titulo.grid(column=0,row=3, padx= 10, pady=10)
    E1 = tk.Entry(janela4)
    E1.grid(column=0, row=4, padx= 10, pady=10)

    text_autor = tk.Label(janela4,text= "Digite o autor do livro:")
    text_autor.grid(column=0,row=5, padx= 10, pady=10)
    E2 = tk.Entry(janela4)
    E2.grid(column=0, row=6, padx= 10, pady=10)

    text_ano = tk.Label(janela4,text= "Digite o ano do livro:")
    text_ano.grid(column=0,row=7, padx= 10, pady=10)
    E3 = tk.Entry(janela4)
    E3.grid(column=0, row=8, padx= 10, pady=10)

    text_titulo = tk.Label(janela4,text= "Digite o título do livro:")
    text_titulo.grid(column=0,row=9, padx= 10, pady=10)
    E1 = tk.Entry(janela4)
    E1.grid(column=0, row=10, padx= 10, pady=10)

    botao_voltar4 = tk.Button(janela4, text="Fechar a janela", command= janela4.destroy)
    botao_voltar4.grid(column=0, row=1, padx=10, pady=10)

    botao_entrar4 = tk.Button(janela4, text="Concluido!", command= janela4.destroy)
    botao_entrar4.grid(column=0, row=11,  padx= 10, pady=10)

def atualizar_livros():
    janela5 = tk.Toplevel()
    janela5.title("Página de atualizar os livros")
    
    text_atualizar = tk.Label(janela5, text="Atualizar um livro!")
    text_atualizar.grid(column=0, row=2, padx= 10, pady=10)

    text_titulo = tk.Label(janela5,text= "Digite o título antigo do livro:")
    text_titulo.grid(column=0,row=3, padx= 10, pady=10)
    E1 = tk.Entry(janela5)
    E1.grid(column=0, row=4, padx= 10, pady=10)

    text_titulo2 = tk.Label(janela5,text= "Digite o novo título do livro:")
    text_titulo2.grid(column=0,row=5, padx= 10, pady=10)
    E2 = tk.Entry(janela5)
    E2.grid(column=0, row=6, padx= 10, pady=10)

    text_autor = tk.Label(janela5,text= "Digite o autor do livro:")
    text_autor.grid(column=0,row=7, padx= 10, pady=10)
    E3 = tk.Entry(janela5)
    E3.grid(column=0, row=8, padx= 10, pady=10)

    text_ano = tk.Label(janela5,text= "Digite o ano do livro:")
    text_ano.grid(column=0,row=9, padx= 10, pady=10)
    E4 = tk.Entry(janela5)
    E4.grid(column=0, row=10, padx= 10, pady=10)

    text_status = tk.Label(janela5,text= "Digite o status do livro:")
    text_status.grid(column=0,row=11, padx= 10, pady=10)
    E5 = tk.Entry(janela5)
    E5.grid(column=0, row=12, padx= 10, pady=10)

    botao_voltar5 = tk.Button(janela5, text="Fechar a janela", command= janela5.destroy)
    botao_voltar5.grid(column=0, row=1, padx=10, pady=10)

    botao_entrar5 = tk.Button(janela5, text="Concluido!", command= janela5.destroy)
    botao_entrar5.grid(column=0, row=13,  padx= 10, pady=10)

def emprestar_livros():
    janela6 = tk.Toplevel()
    janela6.title("Página de emprestar um livro")
    
    text_emprestar = tk.Label(janela6, text="Emprestar um livro!")
    text_emprestar.grid(column=0, row=2, padx= 10, pady=10)

    text_titulo = tk.Label(janela6,text= "Digite o título do livro:")
    text_titulo.grid(column=0,row=3, padx= 10, pady=10)
    E1 = tk.Entry(janela6)
    E1.grid(column=0, row=4, padx= 10, pady=10)

    text_user = tk.Label(janela6,text= "Digite o seu user:")
    text_user.grid(column=0,row=5, padx= 10, pady=10)
    E2 = tk.Entry(janela6)
    E2.grid(column=0, row=6, padx= 10, pady=10)

    botao_voltar6 = tk.Button(janela6, text="Fechar a janela", command= janela6.destroy)
    botao_voltar6.grid(column=0, row=1, padx=10, pady=10)

    botao_entrar6 = tk.Button(janela6, text="Concluido!", command= janela6.destroy)
    botao_entrar6.grid(column=0, row=7,  padx= 10, pady=10)

def devolver_livros():
    janela7 = tk.Toplevel()
    janela7.title("Página de devolver um livro")
    
    text_emprestar = tk.Label(janela7, text="Devolver um livro!")
    text_emprestar.grid(column=0, row=2, padx= 10, pady=10)

    text_titulo = tk.Label(janela7,text= "Digite o título do livro:")
    text_titulo.grid(column=0,row=3, padx= 10, pady=10)
    E1 = tk.Entry(janela7)
    E1.grid(column=0, row=4, padx= 10, pady=10)

    text_user = tk.Label(janela7,text= "Digite o seu user:")
    text_user.grid(column=0,row=5, padx= 10, pady=10)
    E2 = tk.Entry(janela7)
    E2.grid(column=0, row=6, padx= 10, pady=10)

    botao_voltar6 = tk.Button(janela7, text="Fechar a janela", command= janela7.destroy)
    botao_voltar6.grid(column=0, row=1, padx=10, pady=10)

    botao_entrar6 = tk.Button(janela7, text="Concluido!", command= janela7.destroy)
    botao_entrar6.grid(column=0, row=7,  padx= 10, pady=10)

def listar_livros():
    janela8 = tk.Toplevel()
    janela8.title("Lista dos livros")
    
    text_emprestar = tk.Label(janela8, text="Lista!")
    text_emprestar.grid(column=0, row=2, padx= 10, pady=10)

    botao_voltar7 = tk.Button(janela8, text="Fechar a janela", command= janela8.destroy)
    botao_voltar7.grid(column=0, row=1, padx=10, pady=10)

janela = tk.Tk()
janela.title('Sistema Biblioteca')

texto_orientacao1 = Label(janela, text="Bem-vindo!")
texto_orientacao1.grid(column=0, row=0)

texto_orientacao2 = Label(janela, text="Clique no botão para fazer o cadastro: ")
texto_orientacao2.grid(column=0, row=1, padx= 10, pady=10)
botao = tk.Button(janela, text="Clique aqui", command=register)
botao.grid(column=0, row=2, padx= 10, pady=10)

texto_orientacao3 = Label(janela, text="Clique no botão para fazer o login: ")
texto_orientacao3.grid(column=0, row=3, padx= 10, pady=10)
botao2 = tk.Button(janela, text="Clique aqui", command=login)
botao2.grid(column=0, row=4, padx= 10, pady=10)









janela.mainloop()