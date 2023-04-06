from repository.authentication import Auth
from repository.registration import Registration
from fastapi import APIRouter
from repository.users import *
from models.usuario import *

security_router = APIRouter()
    
@security_router.post("/session/token")
def token(usuario: Usuario):
    _login = usuario.login
    _password = usuario.password
    return Auth.authenticate_user(_login, _password)

@security_router.post("/security/create_user")
def create_user(usuario: Usuario):
    _login = usuario.login
    _password = usuario.password
    return Users.create_user(_login, _password)

@security_router.post("/security/update_user")
def update_user(usuario: UsuarioCadastro, token: Token):
    _login = usuario.login
    nickname = usuario.nickname
    level = usuario.level
    _token = token.token
    return Registration.update(_login, nickname, level, _token)