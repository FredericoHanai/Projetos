def soma():
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    if n1.isnumeric() and n2.isnumeric():
        n1 = int(n1)
        n2 = int(n2)
        n3 = n1 + n2
        print(f'A soma entre {n1} e {n2} é igual a  {n3} '.upper())
    else:
        print('\33[31mNão foi digitado um numero válido, insira novamente\33[m')
    print('\33[33m-*-\33[m' * 40)


def subtração():
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    if n1.isnumeric() and n2.isnumeric():
        n1 = int(n1)
        n2 = int(n2)
        n3 = n1 - n2
        print(f'A subtração entre {n1} e {n2} é igual a {n3}'.upper())
    else:
        print('\33[31mNão foi digitado um numero válido, insira novamente\33[m')
    print('\33[33m-*-\33[m' * 40)


def multiplicação():
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    if n1.isnumeric() and n2.isnumeric():
        n1 = int(n1)
        n2 = int(n2)
        n3 = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é igual a {n3}'.upper())
    else:
        print('\33[31mNão foi digitado um numero válido, insira novamente\33[m')
    print('\33[33m-*-\33[m' * 40)


def divisão():
    n1 = input('Digite um numero: ')
    n2 = input('Digite outro numero: ')
    if n1.isnumeric() and n2.isnumeric():
        n1 = int(n1)
        n2 = int(n2)
        n3 = n1 / n2
        print(f'A divisão entre {n1} e {n2} é {n3}'.upper())
    else:
        print('\33[31mNão foi digitado um numero válido, insira novamente\33[m')
    print('\33[33m-*-\33[m' * 40)


while True:
    escolha = int(input('Calculadora, escolha as opcoes:\n'
                        '1 - Soma \n'
                        '2 - Subtração\n'
                        '3 - Multiplcação\n'
                        '4 - Divisão: \n'
                        '0 - STOP\n'
                        'Opção: '))
    if escolha == 1:
        soma()
    elif escolha == 2:
        subtração()
    elif escolha == 3:
        multiplicação()
    elif escolha == 4:
        divisão()
    elif escolha == 0:
        break
    else:
        print('Numero invalido, favor inserir correto')