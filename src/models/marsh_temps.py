from ..app import ma
from ..models import Temps

class TempSchemma(ma.SQLAlchemySchema):
    class Meta:
        model = Temps
    
    telefone = ma.auto_field()
    senha = ma.auto_field()
    nome = ma.auto_field()
    code = ma.auto_field()
    data = ma.auto_field()

temp = TempSchemma()
temps = TempSchemma(many=True)