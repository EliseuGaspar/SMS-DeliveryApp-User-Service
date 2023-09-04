from ..app import db
from datetime import datetime as dt

class Temps(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True, autoincrement = True)
    telefone = db.Column(db.String(10), unique = True)
    senha = db.Column(db.String(255), unique = True)
    nome = db.Column(db.String(255))
    code = db.Column(db.String(7))
    data = db.Column(db.String(30))

    def __repr__(self) -> str:
        return f"UsuarioTemp <{self.nome}>"
    
    def __init__(self, telefone : str, senha : str, nome : str, code : str) -> None:
        self.telefone = telefone
        self.senha = senha
        self.nome = nome
        self.code = code
        self.data = str(dt.now())
    
    def cadastre_se(self) -> None:
        db.session.add(self)
        db.session.commit()
    
    def apague_se(self) -> None:
        db.session.delete(self)
        db.session.commit()