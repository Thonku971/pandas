import pandas as pd
import matplotlib.pyplot as plt

data={
    'Produtos':['Maçã', 'Banana', 'Laranja'],
    'Preços' : [3.5, 2.0, 4.2],
    'Quantidades' : [10, 15, 8]
}

df= pd.DataFrame(data)

df["Total de Vendas"] = df["Preços"] * df["Quantidades"]

df["Imposto"] = df["Total de Vendas"] * 0.05

def classificar_preco(preco):
    return "Alto" if preco > 3 else "Baixo"

df["Categoria Preço"] = df["Preços"].apply(classificar_preco)
print(df)

df["Margem"] = df["Total de Vendas"] - df["Imposto"] #df.apply(lambda row: row["Total de Vendas"] - row["Imposto"], axis=1) pode ser usada em situações mais complexas
print(df)

#Gráfico de Barras (Bar Chart):

#df_grouped_vendas = df.groupby("Produtos")["Total de Vendas"].sum()
#df_grouped_vendas.plot(kind="bar")
#plt.title("Total de Vendas por Produto")
#plt.xlabel("Produto")
#plt.ylabel("Total de Vendas")
#plt.show()

#Gráfico de Pizza (Pie Chart):

#df_grouped_vendas.plot(kind="pie", autopct='%1.1f%%', startangle=90)
#plt.title("Distribuição das Vendas")
#plt.ylabel('')  # Remove o rótulo da legenda
#plt.show()

#Gráfico de Linha (Line Plot):

#df_grouped_vendas.plot(kind="line")
#plt.title("Total de Vendas por Produto (Linha)")
#plt.xlabel("Produto")
#plt.ylabel("Total de Vendas")
#plt.show()

#Histograma:

#df["Preços"].plot(kind="hist", bins=10, edgecolor="black")
#plt.title("Distribuição de Preços")
#plt.xlabel("Preço")
#plt.ylabel("Frequência")
#plt.show()

#Box Plot (Gráfico de Caixa):

#df["Preços"].plot(kind="box")
#plt.title("Box Plot de Preços")
#plt.show()

#Scatter Plot (Gráfico de Dispersão)

#df.plot(kind="scatter", x="Quantidades", y="Preços")
#plt.title("Relação entre Quantidades e Preços")
#plt.xlabel("Quantidades")
#plt.ylabel("Preços")
#plt.show()

#Personalizando Gráficos:

#df_grouped_vendas.plot(kind="bar", color="green", linestyle="--")
#plt.title("Total de Vendas por Produto (Personalizado)")
#plt.xlabel("Produto")
#plt.ylabel("Total de Vendas")
#plt.show()

#Adicionar Legendas e Anotações:
 
#plt.plot(df_grouped_vendas.index, df_grouped_vendas.values, label="Vendas", color="blue")
#plt.legend()
#plt.title("Vendas por Produto com Legenda")
#plt.xlabel("Produto")
#plt.ylabel("Total de Vendas")
#plt.show()

#Exercícios
#Crie um gráfico de barras mostrando o total de vendas por produto.
#Crie um gráfico de linha que mostre a evolução das vendas totais.
#Gere um histograma para a distribuição dos preços dos produtos.
#Crie um gráfico de dispersão para visualizar a relação entre a quantidade de itens e o preço.
#Personalize um gráfico (como alterando as cores ou adicionando uma legenda).

#df_grouped_vendas = df.groupby("Produtos")["Total de Vendas"].sum()
#df_grouped_vendas.plot(kind="bar")
#plt.title("Total de Vendas por Produto")
#plt.xlabel("Produto")
#plt.ylabel("Total de Vendas")
#plt.show()

#df_grouped_vendas = df.groupby("Produtos")["Total de Vendas"].sum()
#df_grouped_vendas.plot(kind="line")
#plt.title("Total de Vendas por Produto (Linha)")
#plt.xlabel("Produto")
#plt.ylabel("Total de Vendas")
#plt.show()

#df["Preços"].plot(kind="hist", bins=10, edgecolor="black")
#plt.title("Distribuição de Preços")
#plt.xlabel("Preço")
#plt.ylabel("Frequência")
#plt.show()


#df.plot(kind="scatter", x="Quantidades", y="Preços")
#plt.title("Relação entre Quantidades e Preços")
#plt.xlabel("Quantidades")
#plt.ylabel("Preços")
#plt.show()

df_grouped_vendas = df.groupby("Produtos")["Total de Vendas"].sum()
df_grouped_vendas.plot(kind="bar", color="blue", linestyle="--")
plt.legend()
plt.title("Vendas por Produto com Legenda")
plt.xlabel("Produto")
plt.ylabel("Total de Vendas")
plt.show()