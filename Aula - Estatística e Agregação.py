import pandas as pd

data={
    'Produtos':['Maçã', 'Banana', 'Laranja'],
    'Preços' : [3.5, 2.0, 4.2],
    'Quantidades' : [10, 15, 8]
}

df= pd.DataFrame(data)

print (df)
# Estatísticas básicas para colunas numéricas
print(df.describe())

# Média de uma coluna específica
print(df["Preços"].mean())

# Soma total de uma coluna
print(df["Quantidades"].sum())

# Mediana de uma coluna
print(df["Preços"].median())

# Valor máximo e mínimo de uma coluna
print(df["Preços"].max())
print(df["Preços"].min())


# Agrupar por uma coluna e calcular a soma
df_grouped = df.groupby("Produtos")["Quantidades"]
print(df_grouped.sum())

# Agrupar por múltiplas colunas e calcular a média
df_grouped_avg = df.groupby(["Produtos", "Preços"])["Quantidades"]
print(df_grouped_avg.mean())

# Aplicando múltiplas funções de agregação
# Substituindo as funções built-in (min, max, sum) por strings
df_grouped_agg = df.groupby("Produtos")["Quantidades"].agg(["min", "max", "sum", "mean"])
print(df_grouped_agg)


# Somar 10 a todos os valores de uma coluna
df["Preços"] = df["Preços"] + 10
print(df)

# Multiplicar todas as quantidades por 2
df["Quantidades"] = df["Quantidades"] * 2
print(df)

# Criar uma nova coluna com o preço total (preço * quantidade)
df["Total"] = df["Preços"] * df["Quantidades"]
print(df)


#Exercícios
#Use o DataFrame de produtos e faça o seguinte:
#Calcule a média de preços e a soma das quantidades.
#Agrupe os produtos pela coluna "Item" e calcule o total de vendas (preço * quantidade).
#Crie uma nova coluna chamada "Imposto" que seja 5% do "Total".
#Aplique várias funções agregadas (como min, max, mean) nas colunas "Preços" e "Quantidades".



data={
    'Produtos':['Maçã', 'Banana', 'Laranja'],
    'Preços' : [3.5, 2.0, 4.2],
    'Quantidades' : [10, 15, 8]
}

df= pd.DataFrame(data)


df_grouped_avg = df["Preços"].mean()
print(df_grouped_avg)
df_grouped_sum = df["Quantidades"].sum()
print(df_grouped_sum)


df["Total de Vendas"] = df["Preços"] * df["Quantidades"]

df_grouped_vendas = df.groupby("Produtos")["Total de Vendas"].sum()

df_grouped_vendas = df_grouped_vendas.reset_index()
print(df_grouped_vendas)


df["Imposto"] = df["Total de Vendas"] * 0.05

df_grouped_vendas = df.groupby("Produtos")["Imposto"].sum()

df_grouped_vendas = df_grouped_vendas.reset_index()
print(df_grouped_vendas)


df_grouped_agg = df.groupby("Produtos")[(["Preços", "Quantidades"])].agg(["min", "max", "sum", "mean"])
print(df_grouped_agg)
