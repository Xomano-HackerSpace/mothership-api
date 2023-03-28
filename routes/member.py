from security.members import Members
from fastapi import APIRouter
from interfaces.models import *
from security.users import *

member_router = APIRouter()
members_creator = Members()
    
@member_router.post("/member")
def Create_Member(membro: MembroInscricao):
    return members_creator.create_member(membro)

def List_Members():
    return members_creator.list_members()
