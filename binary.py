dividendo = int(input("Digite seu numero: "))
quociente = 1
lista = []

while quociente >= 1:
    resto = dividendo % 2
    lista.insert(0,resto)
    quociente = dividendo // 2
    dividendo = quociente
nova_lista = [str(a) for a in lista]
resultado = ("".join(nova_lista))
print(f"O numero {dividendo} convertido para binario é: {resultado}")