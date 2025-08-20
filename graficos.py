# %% 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %%

df = pd.read_csv("data/points_tmw.csv")

df.head()
# %%
group_prod = df.groupby("descProduto")['idTransacao'].count().reset_index().sort_values(by='idTransacao')

group_prod
# %%
plt.bar(group_prod['descProduto'], group_prod['idTransacao'])
plt.show()
# %%
sns.barplot(group_prod,y='descProduto',x='idTransacao')
plt.xlabel('Quantidade de Transações')
plt.ylabel('Produto')

# %%
df['datatTransacao'] = pd.to_datetime(df['dtTransacao']).dt.date
df

# %%
group_data = df.groupby('datatTransacao').agg(
    {
    "qtdPontos": "sum",
    "idTransacao":"count"}
).reset_index()

group_data
# %%
group_data = group_data.sort_values(by='datatTransacao')
group_data
# %%
plt.figure(figsize=(8,6))
plt.plot(group_data['datatTransacao'],group_data['idTransacao'])
plt.title('Serie Histórica de Transações')
plt.ylabel('Qtde. Transações')
plt.show()
# %%

plt.hist(group_data['qtdPontos'],bins=18)
plt.xlabel("Pontos")
plt.ylabel('Frequência')
plt.show()
# %%
plt.boxplot(group_data['qtdPontos'])
plt.title("Box-plot")
plt.show()
# %%

sns.scatterplot(group_data, x='qtdPontos',y='idTransacao')
plt.show()
# %%
