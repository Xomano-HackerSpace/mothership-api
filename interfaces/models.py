from pydantic import BaseModel

class Usuario(BaseModel):
    login: str
    password: str

class UsuarioCadastro(BaseModel):
    levels = {
        0: "ScriptKiddie",
        1: "Member",
        2: "Admin"
    }

    login: str
    nickname: str
    level: levels

class Session(BaseModel):
    token: str