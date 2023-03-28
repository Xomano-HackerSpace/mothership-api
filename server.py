from fastapi import FastAPI
import uvicorn
from routes.security import *
from routes.member import *

class Server():
    
    def __init__(self) -> None:
        self.api = FastAPI()
        self.api.include_router(security_router)
        self.api.include_router(member_router)
        uvicorn.run(self.api, host='0.0.0.0')

if __name__ == '__main__':
    api = Server()