def soma(x, y):
    somatoria = x + y
    print(f'A soma entre {x} e {y} é igual a  {somatoria} '.upper())


def subtração(x, y):
    sub = x - y
    print(f'A subtração entre {x} e {y} é igual a {sub}'.upper())
    print('\33[33m-*-\33[m' * 40)


def multiplicação(x, y):
    multi = x * y
    print(f'A multiplicação entre {x} e {y} é igual a {multi}'.upper())
    print('\33[33m-*-\33[m' * 40)


def divisão(x, y):
    div = x / y
    print(f'A divisão entre {x} e {y} é {div}'.upper())
    print('\33[33m-*-\33[m' * 40)


while True:
    print("CALCULADORA")
    resp = input("Deseja fazer uma operação? S/N: ").upper()
    if resp == "N":
        break
    else:
        n1 = input('Digite um numero: ')
        n2 = input('Digite outro numero: ')
        if n1.isnumeric() and n2.isnumeric():
            n1 = int(n1)
            n2 = int(n2)
            while True:
                escolha = int(input('Escolha a operação:\n'
                                    '1 - Soma \n'
                                    '2 - Subtração\n'
                                    '3 - Multiplcação\n'
                                    '4 - Divisão: \n'
                                    'Opção: '))
                if escolha == 1:
                    soma(n1, n2)
                    break
                elif escolha == 2:
                    subtração(n1, n2)
                    break
                elif escolha == 3:
                    multiplicação(n1, n2)
                    break
                elif escolha == 4:
                    divisão(n1, n2)
                    break
                else:
                    print('Número da operação invalido, por favor inserir correto')
        else:
            print('\33[31mNão foi digitado um número válido, insira novamente\33[m')
        print('\33[33m-*-\33[m' * 40)


