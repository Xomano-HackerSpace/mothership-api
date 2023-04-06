from services.sqlite import SQLite
from models.membro import *

class DbHelper:

    def __init__(self) -> None:
        ##os.path IS FILE
        self.db_file = 'database/db_hackerspace.sqlite'
        self.dbconn = SQLite(self.db_file)

    def get_all_users(self):
        query = "SELECT * FROM USUARIOS"
        rows = self.dbconn.select(query)
        usuarios = []
        user = {}
        for row in rows:
            user['login'] = row[1]
            user['nickname'] = row[2]
            user['level'] = row[3]
            user['status'] = row[4]
            user['blocked'] = row[5]
            user['password'] = row[6]
            usuarios.append(user)
        return usuarios

    
    def get_user(self, login: str):
        query = f"SELECT * FROM USUARIOS WHERE LOGIN = '{login}'"
        return self.dbconn.select(query)

    def create_user(self, _login: str, _status: int, _blocked: int, _password: str):
        query = f"INSERT INTO USUARIOS (id, login, status, blocked, password) VALUES( ? ,'{_login}', '{_status}', '{_blocked}', '{_password}')"
        return self.dbconn.insert(query, (None, ))

    def create_member(self, membro: MembroInscricao):
        query = f"INSERT INTO MEMBROS (id, nome, sobrenome, email, discord, github) VALUES ( ? ,'{membro.nome}', '{membro.sobrenome}', '{membro.email}', '{membro.discord}', '{membro.github}')"
        return self.dbconn.insert(query, (None, ))
    
    def get_all_members(self):
        query = f"SELECT * FROM MEMBROS"
        return self.dbconn.select(query)