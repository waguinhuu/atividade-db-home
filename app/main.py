from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)


    

    while True:
        print("""\n=== SENAI SOLUTION ===\n
        1 - Adicionar usuário\n
        2 - Pesquisar um usuário\n 
        3 - Atualizar dados de um usuário\n 
        4 - Excluir um usuário\n
        5 - Exibir todos os usuários cadastrados\n 
        0 - Sair""")

        opcao = input("Digite a opção desejada: ")

        match(opcao):
            case '1':
                #Solicitando dados do usuario
                print("\nAdicionando usuario: ")
                nome = input("Digite o nome do usuario: ")
                email = input("Digite o email do usuario: ")
                senha = input("Digite a senha do usuario: ")

                service.criar_usuario(nome=nome, email=email, senha=senha)
                
            case '2':
                pesquisarUsuario = input("Digite o email do usuário: ")
                usuario = repository.pesquisar_usuario_por_email(pesquisarUsuario)

                if usuario:
                    print(f"\nUsuário encontrado:\nNome: {usuario.nome}\nEmail: {usuario.email}\n Senha: {usuario.senha}")
                else:
                    print("Usuário não encontrado.")
            
            case '3':
                print("\nAtualizando os dados de um usuario")

                email_usuario = input("Informe o e-mail do usuario")
                usuario = repository.atualizar_dados_do_usuario(email_usuario)

                if usuario:
                
                 usuario.nome = input("Digite seu nome: ")
                 usuario.email = input("Digite seu e-mail: ")
                 usuario.senha = input("Digite sua senha: ")
                 session.commit()

                else:
                    print("Usuario não encontrado.")

            case '4':
                email_usuario = input("Informe o e-mail do usuario: ")
                usuario = repository.pesquisar_usuario_por_email(email_usuario)

                if usuario:
                    repository.excluir_usuario(usuario)
                    print("\nUsuário deletado com sucesso.")
                else:
                    print("Usuário não encontrado.")

            case '5':
               # Exibindo todos os usuarios na tabela usuarios do banco de dados.
                print("\nListando usuarios cadastrados: ")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"\nNome: {usuario.nome} - \nE-mail: {usuario.email} - \nSenha: {usuario.senha}\n")
            
            case '0':
                break

            case _:
                os.system("cls || clear")
                print("Opção invalida. Tente novamente")



            


   

   

if __name__ == "__main__":
    os.system("cls || clear")
    main()