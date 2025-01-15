import pandas as pd

print(pd.DataFrame({'Yes' : [50, 21], 'No' : [131,2] }))

print(pd.DataFrame({'Joao' : ['Sim', 'Não'], 'Maria' : ['Sim', 'Não'] }))

print(pd.DataFrame({'A' : [0, 1], 'B' : [1, 0] }, index=['Entrada 1','Entrada 2']))

print (pd.Series([1,2,3,4,5,6,7,8,9,10]))


print (pd.Series([1,2,3,4,5,6,7,8,9,10], index = ['valor 1','valor 2','valor 3','valor 4','valor 5','valor 6','valor 7','valor 8','valor 9','valor 10'], name='Valores'))


wine_review = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)

print(wine_review.shape)


print(wine_review.head())