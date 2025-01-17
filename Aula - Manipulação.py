import pandas as pd

data={
    'Produtos':['Maçã', 'Banana', 'Laranja'],
    'Preços' : [3.5, 2.0, 4.2],
    'Quantidades' : [10, 15, 8]
}

df= pd.DataFrame(data)

# Selecionar uma única coluna
print(df["Produtos"])

# Selecionar múltiplas colunas
print(df[["Produtos", "Preços"]])

print(df.loc[0])  # Primeira linha

# Selecionar múltiplas linhas (por posição)
print(df.iloc[0:2])  # Da primeira até a segunda linha

# Produtos com preço maior que 3
filtro = df["Preços"] > 3
print(df[filtro])

# Produtos com quantidade maior que 10 e preço menor que 4
filtro = (df["Quantidades"] > 10) & (df["Preços"] < 4)
print(df[filtro])


# Adicionar uma coluna de Total (Preço * Quantidade)
df["Total"] = df["Preços"] * df["Quantidades"]
print(df)


# Remover a coluna "Total"
df = df.drop(columns=["Total"])
print(df)


# Adicionar uma nova linha ao DataFrame
nova_linha = {"Produtos": "Pera", "Preços": 3.0, "Quantidades": 12}
df = df._append(nova_linha, ignore_index=True)
print(df)


# Remover a linha de índice 0
df = df.drop(index=0)
print(df)

df = df.set_index("Produtos")
print(df)


df = df.reset_index()
print(df)


# Exercícios
# Use o DataFrame de produtos e faça o seguinte:
# Filtre apenas os produtos com quantidade maior que 10.
# Adicione uma nova coluna chamada "Desconto", com 10% do preço de cada produto.
# Remova a coluna "Quantidades".
# Adicione um novo produto ao DataFrame, chamado "Uva", com preço 5.0 e quantidade 20.

nova_linha = {"Produtos": "Uva", "Preços": 5.0, "Quantidades": 20}
df = pd.concat([df, pd.DataFrame([nova_linha])], ignore_index=True)
print(df)

filtro = (df["Quantidades"] > 10) 
print(df[filtro])

df["Desconto"] = df["Preços"] * 0.1
print(df)

df = df.drop(columns=["Quantidades"])
print(df)


