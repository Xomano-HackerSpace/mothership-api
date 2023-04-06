from repository.sessions import *
from services.database import DbHelper
from models.membro import *

all_members = []

class Members:

    def __init__(self, membro: MembroInscricao = None) -> None:
        self.db = DbHelper()
        if membro:
            self.membro = membro

    def create_member(self):
        return self.db.create_member(self.membro)

    def list_members(self):
        all_members = self.db.get_all_members()
        members_objs = []
        
        for member in all_members:
            member = MembroInscricao(id=member[0], nome=member[1], sobrenome=member[2], email=member[3], discord=member[4], github=member[5])
            members_objs.append(member)

        return members_objs