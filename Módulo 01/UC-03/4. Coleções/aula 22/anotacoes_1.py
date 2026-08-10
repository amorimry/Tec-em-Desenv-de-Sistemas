fruta = {
    "Nome": "Banana",
    "Preço": 3.5,
    "Estoque": 100
}

# bom para fazer banco de dados, um dict dentro de um dict
frutas = {
    1: {
    "Nome": "Banana",
    "Preço": 3.5,
    "Estoque": 100
},
    2: {
    "Nome": "Maçã",
    "Preço": 2.8,
    "Estoque": 50
}
}
print(frutas[2]["Nome"])