from fastapi import FastAPI
import uvicorn
from routes.security import *

class Server():
    
    def __init__(self) -> None:
        self.api = FastAPI()
        self.api.include_router(security_router)
        uvicorn.run(self.api)

if __name__ == '__main__':
    api = Server()
