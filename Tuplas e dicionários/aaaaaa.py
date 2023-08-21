def suspeito_eh_natural(nome):
    suspeitas = 0
    if "biceps" in cadastro_de_suspeitos[nome]:
        if cadastro_de_suspeitos[nome]["biceps"] > 45:
            suspeitas += 1
    if "tempo" in cadastro_de_suspeitos[nome]:
        if cadastro_de_suspeitos[nome]["tempo"] < 1800:
            suspeitas += 1
    if "frequencia" in cadastro_de_suspeitos[nome]:
        if cadastro_de_suspeitos[nome]["frequencia"] < 4:
            suspeitas += 1
    if "gordura" in cadastro_de_suspeitos[nome]:
        if cadastro_de_suspeitos[nome]["gordura"] < 10:
            suspeitas += 1
    if "suor" in cadastro_de_suspeitos[nome]:
        if not cadastro_de_suspeitos[nome]["suor"]:
            suspeitas += 1
    else:
        suspeitas += 1

    if suspeitas < 3:
        cadastro_de_suspeitos[nome]["natural"] = True
        return True
    cadastro_de_suspeitos[nome]["natural"] = False
    return False

def porcentagem_de_naturais():
    #comentar isso aqui caso sejam apenas os julgados até agora!
    for nome in cadastro_de_suspeitos.keys():
        cadastro_de_suspeitos[nome]["natural"] = suspeito_eh_natural(nome)
    qtd_fake_natty = 0
    for nome in cadastro_de_suspeitos.keys():
        print(cadastro_de_suspeitos[nome])
        if not cadastro_de_suspeitos[nome]["natural"]:
            qtd_fake_natty += 1

    print(qtd_fake_natty)
    porcentagem = qtd_fake_natty / len(cadastro_de_suspeitos) * 100
    porcentagem = int(porcentagem)
    return porcentagem

cadastro_de_suspeitos = {
    "Rodrigo Góes": {
        "biceps": 35, 
        "tempo": 1*60*60, 
        "frequencia": 5,
        "gordura": 12
    },
    "Rayane Gomes": {
        "biceps": 50,
        "tempo": 120, 
        "frequencia": 1
    }
}

print(porcentagem_de_naturais())