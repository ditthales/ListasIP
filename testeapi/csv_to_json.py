import pandas as pd
import json

# Leitura do arquivo CSV
df = pd.read_csv('data_filter.csv')

products_dict = {}
for index, row in df.iterrows():
    products_dict[str(row['gtin14'])] = {'name': row['name']}

# Criar o dicionário final no formato desejado
final_dict = {'products': products_dict}

with open('data.json', 'w') as json_file:
    json.dump(final_dict, json_file, indent=2)

print("fim")

