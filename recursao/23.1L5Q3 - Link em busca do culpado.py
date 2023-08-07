def is_substring(sub, string):
    if len(string) < len(sub):
        return False
    if string[:len(sub)] == sub:
        return True
    return is_substring(sub, string[1:])


nome_do_suspeito = input()
string_concatenada = input()

if is_substring(nome_do_suspeito.lower(), string_concatenada.lower()):
    print(f"Encontrei, o culpado é o {nome_do_suspeito}!")
else:
    print(f"Não era o {nome_do_suspeito}, tenho que continuar procurando.")