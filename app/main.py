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

        match opcao:
            case '1':
                print("\nAdicionando usuário: ")
                nome = input("Digite o nome do usuário: ")
                email = input("Digite o email do usuário: ")
                senha = input("Digite a senha do usuário: ")

                service.criar_usuario(nome=nome, email=email, senha=senha)
                
            case '2':
                email = input("Digite o email do usuário: ")
                service.pesquisar_usuario_por_email(email=email)
            
            case '3':
                print("\nAtualizando os dados de um usuário")
                email_usuario = input("Informe o e-mail do usuário: ")
                nome = input("Digite o novo nome: ")
                email = input("Digite o novo e-mail: ")
                senha = input("Digite a nova senha: ")
                service.atualizar_dados_do_usuario(email_usuario=email_usuario, nome_att=nome, email_att=email, senha_att=senha)

            case '4':
                email_usuario = input("Informe o e-mail do usuário: ")
                service.excluir_usuario(email=email_usuario)

            case '5':
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"\nNome: {usuario.nome} - \nE-mail: {usuario.email} - \nSenha: {usuario.senha}\n")
            
            case '0':
                break

            case _:
                os.system("cls || clear")
                print("Opção inválida. Tente novamente")

if __name__ == "__main__":
    os.system("cls || clear")
    main()
