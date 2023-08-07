def identifica_palindromo(string: str):
    string = string.lower()
    string = string.replace(" ", "")
    palavra_ao_contrário = string[::-1]
    if palavra_ao_contrário == string:
        return True
    else:
        return False

def conta_distintos(string: str):
    string = string.lower()
    unicos = set(string)
    unicos.discard(' ')
    numero = len(unicos)
    return numero

def identifica_se_eh_so_numero(string: str):
    for caractere in string:
        if caractere in "1234567890":
            return True
    return False

numero_de_frases_ou_numeros = int(input())

for _ in range(numero_de_frases_ou_numeros):
    string = input()
    eh_palindromo = identifica_palindromo(string)
    numero_distintos = conta_distintos(string)
    eh_so_numero = identifica_se_eh_so_numero(string)
    if not eh_palindromo:
        print('A frase ou o número não é um palíndromo.')
    else:
        if eh_so_numero:
            print(f'O número "{string}" é um palíndromo!\nHá {numero_distintos} número(s) distinto(s) na sequência de números.')
        else:
            print(f'A frase "{string}" é um palíndromo!\nHá {numero_distintos} letra(s) distinta(s) na frase.')