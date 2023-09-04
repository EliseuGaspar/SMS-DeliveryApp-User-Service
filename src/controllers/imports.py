from flask import request, jsonify, make_response, redirect
from flask_jwt_extended import jwt_required, create_access_token
from os import getenv
import json
from datetime import timedelta
from ..app import app, db, socket
from ..models import Usuario, usuario, Temps
from ..packages.code_generation import Generator