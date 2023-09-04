from ..app import db


class Usuario(db.Model):
    id = db.Column(db.Integer, unique = True, primary_key = True, autoincrement = True)
    telefone = db.Column(db.String(10), unique = True)
    senha = db.Column(db.String(255), unique = True)
    nome = db.Column(db.String(255))
    data_atualizacao = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self) -> str:
        return f"Usuario <{self.nome}>"
    
    def __init__(self, telefone : str, senha : str, nome : str) -> None:
        self.telefone = telefone
        self.senha = senha
        self.nome = nome
    
    def cadastre_se(self) -> None:
        db.session.add(self)
        db.session.commit()
    
    def apague_se(self) -> None:
        db.session.delete(self)
        db.session.commit()


