from .imports import *
from requests import put

@app.put('/<int:id>')
@jwt_required()
def usuario_put(id):

    data = request.json
    resposta = put(
        url = F'http://localhost:2021/sms_user/{data["telefone_antigo"]}',
        json = data,
        headers={'Authorization':F'Bearer {data["token"]}'}
    )
    if resposta.status_code == 200:
        _usuario = Usuario.query.filter_by(id=id).first()
        _usuario.telefone = data['telefone']
        _usuario.nome = data['nome']
        _usuario.senha = data['senha']
        _usuario.cadastre_se()
        return make_response(jsonify({'usuario':json.loads(usuario.dumps(Usuario.query.filter_by(telefone=data['telefone']).first()))}),200)
    else:
        return make_response(jsonify({'usuario':json.loads(usuario.dumps(Usuario.query.filter_by(id=id).first()))}),404)



