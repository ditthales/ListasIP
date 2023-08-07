import pandas as pd

# Ler o arquivo CSV gerado anteriormente
df = pd.read_csv("api_data_filtered.csv")

# Nome do arquivo TXT de saída
output_file = "api_data_formatted.txt"

# Abrir o arquivo de texto em modo de escrita
i = 1
with open(output_file, "w") as txt_file:
    # Iterar pelos registros do DataFrame
    for index, row in df.iterrows():
        print(f"{(i / 715576 * 100):.2f}% concluido")
        # Formatar a linha com gtin14 e name
        line = f'"{row["gtin14"]}":"{row["name"]}",'
        # Escrever a linha no arquivo de texto
        txt_file.write(line + "\n")
        i+=1