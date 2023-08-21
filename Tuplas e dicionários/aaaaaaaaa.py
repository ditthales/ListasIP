string = "BF: 20%"
nova_lista = string.split(" ")
nova_lista[1] = nova_lista[1][:-1]

print(int(nova_lista[1]))