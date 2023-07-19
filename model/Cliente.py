from pydantic import BaseModel
from typing import Optional

class Cliente(BaseModel):
    codigo: Optional[int] = None
    nome: str
    cpf: int
    email: str
    senha: str