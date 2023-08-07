import pandas as pd

# Ler o arquivo CSV gerado anteriormente
df = pd.read_csv("api_data_filtered.csv")

# Filtrar os itens com a quantidade de caracteres no gtin14 igual a 13
df_filtered = df[df['gtin14'].astype(str).str.len() == 13]

# Salvar o resultado em um novo arquivo CSV
df_filtered.to_csv('data_filter.csv', index=False)

print("pronto")