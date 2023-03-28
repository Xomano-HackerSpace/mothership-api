from security.sessions import *
from database.database import DbHelper
from interfaces.models import *
import hashlib

all_users = {} #Implementar observer pra guardar no banco de dados.

class Members:

    def __init__(self) -> None:
        self.db = DbHelper()


    def create_member(self, membro: MembroInscricao):
        self.db.create_member(membro.nome, membro.sobrenome, membro.email, membro.discord, membro.github)
        return 