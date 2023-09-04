from .imports import *
from ..client import enviar #DOC/ServicoUsuario -> pág() parag()
from ..packages.formate_date import formate #DOC/API.pdf -> pág() parag()
from werkzeug.security import generate_password_hash
from requests import post


@app.post('/') # URI para cadastro de usuários
@jwt_required()
def usuario_post():
    data = request.json
    codigo = Generator() # Este método gera o código que será enviado para o usuário
    try:
        new_usuario = Temps(data['telefone'],data['senha'],data['nome'],codigo) # Modelo do usuário na tabela temporaria
        new_usuario.cadastre_se() # Método de cadastro
        resposta = post(
        url = F'http://localhost:2021/enviar_codigo',
        json = {
            "telefone" : data['telefone'],
            "codigo": codigo
        },
        headers={'Authorization':F'Bearer {data["token"]}'}
        )
        if resposta.status_code == 200:
            return make_response(jsonify({
                'usuario':True,
                'tempo':'02:00'
            }),200)
        else:
            return make_response(jsonify({
                'usuario':False,
                'tempo':'00:00'
            }),404)
    except:
        return make_response(jsonify({'usuario':False}),500)


@app.post('/confirm') #URI de confirmacão de cadastro
@jwt_required()
def confirm_():
    usuario_ = Temps.query.filter_by(code=request.json['codigo']).first()
    if usuario_:
        if formate(usuario_.data) >= 2: # formate método -> formata e compara o tempo de cadastro com atual | retorna os minutos passados
            return make_response(jsonify({'confirm':False}),410)
        new_usuario = Usuario(usuario_.telefone,usuario_.senha,usuario_.nome)
        new_usuario.cadastre_se()
        usuario_.apague_se()
        return make_response(jsonify({'usuario':json.loads(usuario.dumps(Usuario.query.filter_by(telefone=usuario_.telefone).first()))}),200)
    else:
        return (jsonify({'confirm':None}),404)

@app.post('/re-codigo') # URI para reenvio do código de confirmção do usuários
@jwt_required()
def re_codigo():
    from datetime import datetime
    data = request.json
    codigo = Generator() # Este método gera o código que será enviado para o usuário
    try:
        usuario_ = Temps.query.filter_by(telefone=data['telefone']).first()
        usuario_.code = codigo
        usuario_.data = datetime.now()
        usuario_.cadastre_se() # Método de cadastro e atualização
        resposta = post(
        url = F'http://localhost:2021/enviar_codigo',
        json = {
            "telefone" : data['telefone'],
            "codigo": codigo
        },
        headers={'Authorization':F'Bearer {data["token"]}'}
        )
        if resposta.status_code == 200:
            return make_response(jsonify({
                'usuario':True,
                'tempo':'02:00'
            }),200)
        else:
            return make_response(jsonify({
                'usuario':False,
                'tempo':'00:00'
            }),404)
    except:
        return make_response(jsonify({'usuario':False}),500)
