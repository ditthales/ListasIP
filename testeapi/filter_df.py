import pandas as pd

# Ler o arquivo CSV gerado anteriormente
df = pd.read_csv("api_data.csv")

# Criar um novo DataFrame contendo apenas as colunas "gtin14" e "name"
df_filtered = df[["gtin14", "name"]]

# Exibir o novo DataFrame
print(df_filtered)

df_filtered.to_csv("api_data_filtered.csv", index=False)
