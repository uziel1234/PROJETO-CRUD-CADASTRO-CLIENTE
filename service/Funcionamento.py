from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

lista_de_cliente = []

class Cliente(BaseModel):
    codigo: Optional[int] = None
    nome: str
    cpf: int
    email: str
    senha: str

@app.get("/get_imprimir_todos_clientes")
def get_imprimir_todos_clientes():
    return lista_de_cliente

@app.post("/post_cadastrar_cliente")
def post_cadastrar_cliente(cliente: Cliente):
 
    lista_de_cliente.append(cliente)
    cliente.codigo = len(lista_de_cliente) - 1 
    return cliente

@app.put("/put_atualizar_email/{codigo}")
def put_atualizar_email(codigo:int,cliente: Cliente):
    encontrar_cliente = lista_de_cliente[codigo]
    encontrar_cliente.email = cliente.email
    return cliente

@app.delete("/delete_deletar_cliente/{codigo}")
def delete_deletar_cliente(codigo:int):
    del lista_de_cliente[codigo]
    return {"mensagem": "cliente deletado com sucesso"}


    


