from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class MembroInscricao(BaseModel):
    id: int | None
    nome: str
    sobrenome: str | None
    email: str | None
    discord: str | None
    github: str | None
