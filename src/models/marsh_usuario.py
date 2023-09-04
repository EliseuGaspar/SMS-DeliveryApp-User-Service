from ..app import ma
from .usuario import Usuario


class UsuarioSchemma(ma.SQLAlchemySchema):
    class Meta:
        model = Usuario
    
    id = ma.auto_field()
    telefone = ma.auto_field()
    senha = ma.auto_field()
    nome = ma.auto_field()
    data_atualizacao = ma.auto_field()

usuario = UsuarioSchemma()
usuarios = UsuarioSchemma(many=True)