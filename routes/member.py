from repository.members import *
from fastapi import APIRouter
from models.membro import *

member_router = APIRouter()
    
@member_router.post("/member")
def Create_Member(membro: MembroInscricao, token):
    new_member = Members(membro)
    return new_member.create_member()

@member_router.get("/listmembers", response_model=list[MembroInscricao])
def List_Members():
    members = Members()
    return members.list_members()
