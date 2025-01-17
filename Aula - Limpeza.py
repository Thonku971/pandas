import pandas as pd

data={
    'Produtos':['Maçã', 'Banana', 'Laranja'],
    'Preços' : [3.5, 2.0, 4.2],
    'Quantidades' : [10, 15, 8]
}

df= pd.DataFrame(data)


# Verificar valores nulos
print(df.isnull())


# Remover todas as linhas com valores nulos
df = df.dropna()
print(df)

# Remover colunas com valores nulos
df = df.dropna(axis=1)
print(df)


# Preencher valores nulos com um valor específico (ex: 0 ou "Desconhecido")
df["Quantidades"] = df["Quantidades"].fillna(0)

# Remover linhas duplicadas
df = df.drop_duplicates()
print(df)


# Remover duplicatas com base na coluna "Produtos"
df = df.drop_duplicates(subset=["Produtos"])
print(df)


# Alterar tipo de dado da coluna "Preços" para inteiro
df["Preços"] = df["Preços"].astype(int)
print(df)


# Renomear a coluna "Preços" para "Valor"
df = df.rename(columns={"Preços": "Valor"})
print(df)

# Renomear o índice para um novo nome
df = df.rename(index={0: "Primeiro", 1: "Segundo", 2: "Terceiro"})
print(df)


# Exercícios
# Crie um DataFrame com alguns valores nulos e faça o seguinte:
# Preencha os valores nulos com "Desconhecido" (se for uma coluna de texto) ou 0 (se for numérica).
# Remova as duplicatas com base em uma coluna de sua escolha.
# Altere o tipo da coluna de preço para float e depois para int.
# Renomeie a coluna "Produtos" para "Item" e os índices para algo mais descritivo (exemplo: "Item 1", "Item 2", etc.).
data={
    'Produtos':[None, 'Banana', None],
    'Preços' : [3.5, None, 4.2],
    'Quantidades' : [10, 15, None]
}
df = pd.DataFrame(data)
print(df.isnull())


df["Preços"] = df["Preços"].fillna(0)
df['Quantidades'] = df['Quantidades'].fillna(0)
df['Produtos'] = df['Produtos'].fillna('Desconhecido')
print(df)

df = df.drop_duplicates()
print(df)

df["Preços"] = df["Preços"].astype(float)
print(df)

df["Preços"] = df["Preços"].astype(int)
print(df)

df = df.rename(columns={"Produtos": "Item"})
df = df.rename(index={0: "Item 1", 1: "Item 2", 2: "Item 3"})
print(df)
