from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

usuarios = [
    {"id": 1, "nome": "Lucas Rodrigues Tavares", "idade": 27},
    {"id": 2, "nome": "Ana Paula Martins", "idade": 31},
    {"id": 3, "nome": "Bruno Henrique Silva", "idade": 24},
    {"id": 4, "nome": "Carla Fernanda Costa", "idade": 29},
    {"id": 5, "nome": "Diego Moreira Lima", "idade": 35},
    {"id": 6, "nome": "Elaine Souza Rocha", "idade": 26},
    {"id": 7, "nome": "Fábio César Almeida", "idade": 40},
    {"id": 8, "nome": "Giselle Ribeiro Duarte", "idade": 22},
    {"id": 9, "nome": "Henrique Bastos Nunes", "idade": 33},
    {"id": 10, "nome": "Isabela Cristina Lopes", "idade": 28}
]

produtos = [
    {"id": 1, "nome": "Cola Branca", "preço": 5.40},
    {"id": 2, "nome": "Lapis", "preço": 0.50},
    {"id": 3, "nome": "Lapizeira", "preço": 4.50},
    {"id": 4, "nome": "Caneta", "preço": 1.50},
    {"id": 5, "nome": "Caderno", "preço": 15},
    {"id": 6, "nome": "Tesoura", "preço": 9.70},
    {"id": 7, "nome": "Mochila", "preço": 45},
    {"id": 8, "nome": "Regua", "preço": 6.20},
    {"id": 9, "nome": "Estojo", "preço": 33},
    {"id": 10, "nome": "Borracha", "preço": 28}
]

# Codigo api Users

@app.get("/")
def read_root():
    return {"mensagem": "Seja bem-vindo à minha API, para usuários, acesse a rota /api/users"}

@app.get("/api/users")
def get_users():
    with open("users.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    return dados

@app.get("/api/v2/users/{user_id}")
def get_users_v2(user_id: int):
    for usuario in usuarios:
        if usuario["id"] == user_id:
            return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.get("/api/v3/users")
def get_users_v3(nome: str = ""):
    
    if nome:
        nome = nome.lower()
        usuarios_filtrados = []       
        for usuario in usuarios:
            nome_usuario = usuario["nome"].lower()
            
            if nome in nome_usuario:
                usuarios_filtrados.append(usuario)
        
        return usuarios_filtrados
   
    return usuarios

# Codigo api Produtos

@app.get("/api/v2/produtos")
def get_produtos_v2():
    with open("produtos.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    return dados

@app.get("/api/v2/produtos/{produtos_id}")
def get_produtos_v3(produtos_id: int):
    with open("produtos.json", "r", encoding="utf-8") as file:
        produtos = json.load(file)

    for produto in produtos:
        if produto["id"] == produtos_id:
            return produto
        

    