from src.app import socket, app
from src.controllers import *
from src.events import *
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    socket.run(
        app=app,
        host='0.0.0.0',
        port=2020,
        debug=True
    )