import ast

def menu():
    print("CONVERSOR DE NÚMEROS 2")
    opcao = int(input("1 -> Decimal para Hexadecimal\n"
                      "2 -> Hexadecimal para Decimal\n"
                      "Escolha o tipo de conversão desejado: "))
    if opcao == 1:
        dec_hexa()
    elif opcao == 2:
        hexa_dec()
    else:
        print("Opção inválida!!\n")
        menu()


def dec_hexa():
    dividendo = int(input("Digite um numero decimal: "))
    div = dividendo
    quociente = 1
    lista = []

    while quociente >= 1:
        resto = dividendo % 16
        lista.insert(0, resto)
        quociente = dividendo // 16
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


def hexa_dec():
    hexa = input("Digite um numero hexadecimal: ").upper()
    hexaList = list(reversed(hexa))
    dec = 0
    hexadecimais = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    for i in hexaList:
        if i.isnumeric():
            calculo = int(i)
            indice = hexaList.index(i)
            dec += calculo*(16**indice)
        else:
            valorLetra = hexadecimais[i]
            indice = hexaList.index(i)
            dec += valorLetra*(16**indice)

    print(f"O numero hexadecimal {hexa} convertido para decimal é {dec}")


if __name__ == "__main__":
    menu()
