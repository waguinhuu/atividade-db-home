from models.usuario_model import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)
            cadastrado = self.repository.pesquisar_usuario_por_email(usuario.email)

            if cadastrado:
                print("Usuário já cadastrado!")
                return
            
            self.repository.salvar_usuario(usuario=usuario)
            print("Usuário cadastrado com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuario()
    
    def pesquisar_usuario_por_email(self, email: str):
        try:
            usuario = self.repository.pesquisar_usuario_por_email(email=email)

            if usuario:
                print(f"\nUsuário encontrado:\nNome: {usuario.nome}\nEmail: {usuario.email}\nSenha: {usuario.senha}")
            else:
                print("Usuário não encontrado.")
    
        except TypeError as erro:
            print(f"Erro ao pesquisar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def excluir_usuario(self, email: str):
        try:
            usuario = self.repository.pesquisar_usuario_por_email(email=email)

            if usuario:
                self.repository.excluir_usuario(usuario)
                print("\nUsuário deletado com sucesso.")
            else:
                print("Usuário não encontrado.")

        except TypeError as erro:
            print(f"Erro ao deletar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def atualizar_dados_do_usuario(self, email_usuario: str, nome_att: str, email_att: str, senha_att: str):
        try:
            usuario = self.repository.pesquisar_usuario_por_email(email=email_usuario)

            if usuario:
                usuario.nome = nome_att
                usuario.email = email_att
                usuario.senha = senha_att
                self.repository.salvar_usuario(usuario)
                print("Dados do usuário atualizados com sucesso!")
            else:
                print("Usuário não encontrado.")

        except TypeError as erro:
            print(f"Erro ao atualizar os dados do usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
