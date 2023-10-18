import pandas as pd

# Carregar os dados
dados = pd.read_csv('C:/Users/julii/Downloads/Teste/pdf.csv')

# Agrupar os dados por município
grupos = dados.groupby('a')

# Para cada município, salvar os dados em um arquivo CSV separado
for nome, grupo in grupos:
    grupo.to_csv(f'{nome}.csv', index=False)
