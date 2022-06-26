def menu():
    print("CONVERSOR DE NÚMEROS")
    opcao = int(input("1 -> Decimal para Binário\n"
                      "2 -> Binário para Decimal\n"
                      "Escolha o tipo de conversão desejado: "))
    if opcao == 1:
        decimalBinario()
    elif opcao == 2:
        binarioDecimal()
    else:
        print("Opção inválida!!\n")
        menu()


def decimalBinario():
    dividendo = int(input("Digite um número decimal: "))
    div = dividendo
    quociente = 1
    lista = []

    while quociente >= 1:
        resto = dividendo % 2
        lista.insert(0, resto)
        quociente = dividendo // 2
        dividendo = quociente
    nova_lista = [str(a) for a in lista]
    resultado = ("".join(nova_lista))
    print(f"O numero {div} convertido para binario é: {resultado}")


def binarioDecimal():
    numBin = input("Digite um número binário: ")
    listBin = list(numBin)
    decimal = 0
    multi = len(listBin) - 1
    for i in listBin:
        n = int(i)
        decimal += n*(2**multi)
        multi -= 1
    print(f"O numero {numBin} convertido para decimal é {decimal}")


if __name__ == "__main__":
    menu()
