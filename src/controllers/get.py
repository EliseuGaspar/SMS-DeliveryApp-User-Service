from .imports import *


@app.get('/')
def index():
    return jsonify(
        {'msg':'DeliveryApp => User Service'}
    )


@app.get('/<int:id>')
async def usuario_get(id):
    try:
        return jsonify({'usuario':json.loads(usuario.dumps(Usuario.query.filter_by(id=id).first()))})
    except:
        return jsonify({'usuario':False})


@app.get('/login')
def login():
    dados = request.json
    if dados['key'] == getenv('key'):
        return jsonify({'token':create_access_token(dados['key'],expires_delta=timedelta(minutes=60))})
    else:
        return jsonify({'token':False})

@app.before_request
def inicializar_banco_de_dados():
    db.create_all()

