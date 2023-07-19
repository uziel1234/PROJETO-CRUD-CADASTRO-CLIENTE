# PROJETO-CRUD-CADASTRO-CLIENTE
Sistema tem como o objetivo de cadastrar, listar, atualizar e deletar clientes





<p align="center">
	<a href="https://www.python.org/">
	  <img alt="python" src="https://img.shields.io/static/v1?color=red&label=Dev&message=python&style=for-the-badge&logo=python">
	</a>
</p>

# ⛏  Tech & Dependências

### Pré-requisitos

*   Python 3.10.11
*   Running uvicorn 0.23.1 


## Clonando o serviço

```sh
git clone https://github.com/uziel1234/PROJETO-CRUD-CADASTRO-CLIENTE.git
 
```

# Executando o serviço

Na pasta raiz do projeto executar o comando:

```sh
  uvicorn main:app
```

<hr>


<hr>

### Doc Swagger:

```sh
http://127.0.0.1:8080/docs
```

Minimun Payload in POST: http://127.0.0.1:8000/post_cadastrar_cliente
```JSON
{ "nome": "ziel",
    "cpf": 1111,
    "email": "xpto@xpto.com",
    "senha": "12345"}
```

