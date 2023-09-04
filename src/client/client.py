import socketio

client = socketio.Client()


def enviar(dados : dict):
    if not client.connected:
        client.connect('http://localhost:2021')
    client.emit('confirmation-p', dados)
    return 1

def atualizar(dados : dict) -> bool:
    if not client.connected:
        client.connect('http://localhost:2021')
    client.emit('atualizar_dados_usuario', dados)


