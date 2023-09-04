from .imports import *
from requests import delete

@app.delete('/<int:id>')
@jwt_required()
def usuario_delete(id):
    
    data = request.json
    usuario_ = Usuario.query.filter_by(id=id).first()
    resposta = delete(
    url = F'http://localhost:2021/sms_user/{usuario_.telefone}',
    headers={'Authorization':F'Bearer {data["token"]}'}
    )
    usuario_.apague_se()
    if resposta.status_code == 200:
        return make_response(jsonify({'usuario':resposta.json()['sms']}),200)
    return make_response(jsonify({'usuario':[]}),404)
    