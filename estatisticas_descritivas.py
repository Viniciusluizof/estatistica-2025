# %%

import pandas as pd

df = pd.read_csv("data/points_tmw.csv")
df.head()
# %%

print('Estatisticas de posição para transações:')
minimo =  df['qtdPontos'].min()
print(f'Minimo: {minimo}')

media = df['qtdPontos'].mean()
print(f'Média: {media}')

quartil_1 = df['qtdPontos'].quantile(0.25)
print(f'1º Quartil: {quartil_1}')

mediana = df['qtdPontos'].median()
print(f'Mediana: {quartil_1}')

quartil_3 = df['qtdPontos'].quantile(0.75)
print(f'3º Quartil: {quartil_3}')

maximo = df['qtdPontos'].max()
print(f'Máximo: {maximo}')

variancia = df['qtdPontos'].var()
print(f'Variânca: {variancia}')

desvio = df['qtdPontos'].std()
print(f'Desvio Padrão: {desvio}')

amplitude = df['qtdPontos'].max() - df['qtdPontos'].min()
print(f'Amplitude: {amplitude}')

df['qtdPontos'].describe().round(2)
# %%


# %%

print('-'*20)
usuarios = df.groupby(['idUsuario']).agg(
                {"idTransacao":"count",
                "qtdPontos": "sum"}
            ).reset_index()

usuarios
# %%
usuarios[["idTransacao","qtdPontos"]].describe().round(2)
