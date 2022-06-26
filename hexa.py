dividendo = int(input("Digite seu numero: "))
div = dividendo
quociente = 1
lista = []

while quociente >= 1:
    resto = dividendo % 16
    lista.insert(0, resto)
    quociente = dividendo //16
    dividendo = quociente

    for i in range(len(lista)):
        if lista[i] == 10:
            lista[i] = str('A')
        elif lista[i] == 11:
            lista[i] == str('B')
        elif lista[i] == 12:
            lista[i] = str('C')
        elif lista[i] == 13:
            lista[i] = str('D')
        elif lista[i] == 14:
            lista[i] = str('E')
        elif lista[i] == 15:
            lista[i] = str('F')


nova_lista = [str(a) for a in lista]
resultado = ("".join(nova_lista))
print(f"O numero {div} convertido para hexadecimal é: {resultado}")