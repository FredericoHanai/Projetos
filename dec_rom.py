def DecimaltoRoman():
    num = int(input("Digite um numero decimal até 4 algarismos: "))

    m = num // 1000
    c = (num // 100) % 10
    d = (num % 100)//10
    u = num % 10

    uni = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    dez = ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    cen = ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    mil = ["M", "MM", "MMM"]

    num_romano = []
    if m > 0:
        num_romano.append(mil[m-1])
    if c > 0:
        num_romano.append(cen[c-1])
    if d > 0:
        num_romano.append(dez[d-1])
    if u > 0:
        num_romano.append(uni[u-1])

    print(f"O número {num} em algarismo romano é:", ''.join(num_romano))

def RomantoDecimal():
    print('CONVERSOR')

    resp = input("Digite o numero romano: ").upper()

    token = False
    valor = 0

    romanos = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40,
               "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000}

    for i in range(len(resp)):
        if token:
            token = False
            continue
        try:
            nAtual = resp[i]
            nProx = resp[i + 1]
            if romanos[nAtual] < romanos[nProx]:
                valor += romanos[nAtual + nProx]
                token = True
                continue
        except:
            valor += romanos[nAtual]
            continue
        valor += romanos[nAtual]
    print(f'O numero ROMANO {resp} em DECIMAL é: {valor}\n')

while True:
    print("Qual das opcões vc deseja:\n"
          "0 - Transformar DECIMAL em ROMANO\n"
          "1 - Tranformar ROMANO em DECIMAL")
    resp = input("Digite sua escolha: ")
    if resp.isnumeric():
        resp = int(resp)
        if resp == 0:
            DecimaltoRoman()
        elif resp == 1:
            RomantoDecimal()
        else:
            print('\n\33[31m Numero inválido, favor colocar 0 ou 1.\33[m\n')
    else:
        print("\n\33[31m Comando invalido!\33[m\n")
