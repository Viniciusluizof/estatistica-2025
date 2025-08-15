# %%

import pandas as pd
import sqlalchemy

# %%
df = pd.read_csv(r"data\points_tmw.csv")

df.head()

engine = sqlalchemy.create_engine("sqlite:///data/tmw.db")

df.to_sql('points', engine,if_exists='replace',index=False)
# %%
pd.value_counts(df['descProduto'])
# %%
freq_produto = df.groupby(['descProduto'])[['idTransacao']].count()
freq_produto
# %%
freq_produto['Freq. Abs. Acumulada'] = freq_produto['idTransacao'].cumsum()

freq_produto
# %%
freq_produto['Freq. Relativa'] = (freq_produto['idTransacao']/freq_produto['idTransacao'].sum())*100

freq_produto
# %%
freq_produto['Freq. Relativa Acumulada'] = freq_produto['Freq. Relativa'].cumsum()
freq_produto
# %%
freq_cat_prod = df.groupby(['descCategoriaProduto'])[['idTransacao']].count()

# %%
freq_cat_prod['Freq. Abs. Acumulada'] = freq_cat_prod['idTransacao'].cumsum()
freq_cat_prod['Freq. Relativa'] = (freq_cat_prod['idTransacao']/freq_cat_prod['idTransacao'].sum())*100
freq_cat_prod['Freq. Relativa Acumulada'] = freq_cat_prod['Freq. Relativa'].cumsum()
freq_cat_prod
# %%
