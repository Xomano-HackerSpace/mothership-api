from pydantic import BaseModel


class MembroInscricao(BaseModel):
    id: int | None
    nome: str
    sobrenome: str | None
    email: str | None
    discord: str | None
    github: str | None
