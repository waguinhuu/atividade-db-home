from models.usuario_model import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self, session: Session):
        self.session = session
    
    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()

    def pesquisar_usuario_por_email(self, email: str):
        return self.session.query(Usuario).filter_by(email = email).first()
    
    def excluir_usuario(self, usuario: Usuario):
        self.session.delete(usuario)
        self.session.commit()

    def listar_usuario(self):
        return self.session.query(Usuario).all()
    
    def atualizar_dados_do_usuario(self, email: str):
        return self.session.query(Usuario).filter_by(email = email).first()