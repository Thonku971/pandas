import pandas as pd

# Criando uma Series
data = [10, 20, 30, 40]
series = pd.Series(data, index=["a", "b", "c", "d"])
print(series)

# Criando um DataFrame
data = {
    "Nome": ["Ana", "Bruno", "Carlos"],
    "Idade": [25, 30, 35],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}
df = pd.DataFrame(data)
print(df)


# Criando um DataFrame com listas
data = [
    ["Ana", 25, "São Paulo"],
    ["Bruno", 30, "Rio de Janeiro"],
    ["Carlos", 35, "Belo Horizonte"]
]
df = pd.DataFrame(data, columns=["Nome", "Idade", "Cidade"])
print(df)


# Mostrar as 5 primeiras linhas
print('inicio', df.head())

# Mostrar as 5 últimas linhas
print('fim', df.tail())


# Exercícios
# Crie uma Series com os números de 1 a 5 e rótulos personalizados (ex: "um", "dois", etc.).
# Crie um DataFrame com os seguintes dados:
# Produtos: "Maçã", "Banana", "Laranja".
# Preços: 3.5, 2.0, 4.2.
# Quantidades: 10, 15, 8.

dados=[1,2,3,4,5]
series = pd.Series(dados, index =['Um', 'Dois', 'Três', 'Quatro', 'Cinco'])
print(series)

data={
    'Produtos':['Maçã', 'Banana', 'Laranja'],
    'Preços' : [3.5, 2.0, 4.2],
    'Quantidades' : [10, 15, 8]
}

df= pd.DataFrame(data)
print(df)


