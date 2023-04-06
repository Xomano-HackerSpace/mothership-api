from pydantic import BaseModel

class Usuario(BaseModel):
    login: str
    password: str


class UsuarioCadastro(BaseModel):
    login: str
    nickname: str
    level = {
        0: "ScriptKiddie",
        1: "Member",
        2: "Admin",
        3: "Padawan"
    }

class Token(BaseModel):
    token: str