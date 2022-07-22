lista = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
placa = input("Digite sua placa: ").upper()

if (placa[0] in lista) and (placa[1] in lista) and (placa[2] in lista):
    print('modelo Brasil')
elif (placa[0] in lista) and (placa[1] in lista) and (placa[2] in lista) and (placa[4] in lista):
    print('mercosul')
else:
    print("invalido")


