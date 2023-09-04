from flask import jsonify
from ..app import socket
from ..models import Usuario, usuario
from ..packages.connection import db
from os import getenv


@socket.on('confirmation-r')
def cadastrar_usuario(data):
    print(data)

@socket.on('atualizar_dados_usuario-r')
def resposta(dados):
    if dados['resposta']:
        dados = dados['dados']
        cursor = db.cursor()
        linhas = cursor.execute(F"""UPDATE `usuarios` SET nome = '{dados["nome"]}', senha = '{dados["senha"]}' telefone = '{dados["telefone"]}' WHERE id = {dados["id"]}""")
        db.commit()
        if linhas > 0:
            pass
        else:
            pass