from fastapi import FastAPI
import uvicorn
from repository import *
from services import database
from routes import member, security

class Server():
    
    def __init__(self) -> None:
        self.api = FastAPI()
        self.api.include_router(member.member_router)
        self.api.include_router(security.security_router)
        uvicorn.run(self.api)
        

if __name__ == '__main__':
    api = Server()