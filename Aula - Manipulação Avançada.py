import pandas as pd

data={
    'Produtos':['Maçã', 'Banana', 'Laranja'],
    'Preços' : [3.5, 2.0, 4.2],
    'Quantidades' : [10, 15, 8]
}

df= pd.DataFrame(data)

df["Total de Vendas"] = df["Preços"] * df["Quantidades"]

df["Imposto"] = df["Total de Vendas"] * 0.05

# Exemplo de tabela pivotada
df_pivot = df.pivot_table(values="Total de Vendas", index="Produtos", columns="Quantidades", aggfunc="sum", fill_value=0)
print(df_pivot)


# Configurando um MultiIndex
df_multi = df.set_index(["Produtos", "Quantidades"])
print(df_multi)

# Selecionar linhas em um MultiIndex (Maçã com Quantidade =10)
print(df_multi.loc[("Maçã", 10)])


# Aplicar uma função para calcular a categoria de preço
def classificar_preco(preco):
    return "Alto" if preco > 3 else "Baixo"

df["Categoria Preço"] = df["Preços"].apply(classificar_preco)
print(df)

# Calcular uma métrica personalizada para cada linha
df["Margem"] = df["Total de Vendas"] - df["Imposto"] #df.apply(lambda row: row["Total de Vendas"] - row["Imposto"], axis=1) pode ser usada em situações mais complexas
print(df)


# Criando um segundo DataFrame
data_extra = {
    "Produtos": ["Maçã", "Banana", "Laranja"],
    "Fornecedor": ["A", "B", "C"]
}
df_extra = pd.DataFrame(data_extra)

# Mesclando os DataFrames
df_merged = pd.merge(df, df_extra, on="Produtos")
print(df_merged)


# Concatenar DataFrames verticalmente
df_concat = pd.concat([df, df_extra], axis=0)
print(df_concat)


#Exercícios
#Crie uma tabela pivotada usando "Produtos" como índice e "Categoria Preço" como coluna.
#Adicione um índice hierárquico ao DataFrame usando as colunas "Produtos" e "Categoria Preço".
#Escreva uma função personalizada que avalie o lucro líquido (Total de Vendas - Imposto) e adicione uma coluna "Lucro".
#Crie um novo DataFrame com informações adicionais (como fornecedor ou região) e mescle com o DataFrame original.

print("\n Exercícios \n")

data={
    'Produtos':['Maçã', 'Banana', 'Laranja'],
    'Preços' : [3.5, 2.0, 4.2],
    'Quantidades' : [10, 15, 8]
}

df= pd.DataFrame(data)

df["Total de Vendas"] = df["Preços"] * df["Quantidades"]

df["Imposto"] = df["Total de Vendas"] * 0.05

df["Categoria Preço"] = df["Preços"].apply(classificar_preco)
print(df ,'\n')

# Calcular uma métrica personalizada para cada linha
df["Margem"] = df["Total de Vendas"] - df["Imposto"] #df.apply(lambda row: row["Total de Vendas"] - row["Imposto"], axis=1) pode ser usada em situações mais complexas
print(df ,'\n')


df_pivot = df.pivot_table(values="Preços", index="Produtos", columns="Categoria Preço", aggfunc="sum", fill_value=0)
print(df_pivot ,'\n')


df_multi = df.set_index(["Produtos", "Categoria Preço"])
print(df_multi ,'\n')


def lucro(row):
    return row["Total de Vendas"] - row["Imposto"]

df["Lucro"] = df.apply(lucro, axis =1)
print(df ,'\n')


data_novo={
    'Produtos':['Maçã', 'Banana', 'Laranja'],
    'Fornecedor' : ["João","Maria","José"],
    'Região' : ["Paraná","São Paulo","Goiás"]
}

df_novo = pd.DataFrame(data_novo)

# Mesclando os DataFrames
df_mesclado = pd.merge(df, df_novo, on="Produtos")
print(df_mesclado ,'\n')
