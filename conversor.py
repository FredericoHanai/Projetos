print('Conversor numérico')

resp = input("Digite o numero romano: ").upper()

token = False
valor = 0

romanos = {"I": 1, "IV" : 4, "V" : 5, "IX" : 9, "X" : 10 , "XL" : 40,
        "L" : 50, "XC" : 90, "C" : 100, "CD" : 400, "D" : 500, "CM" : 900, "M" : 1000}

for i in range(len(resp)):
    if token:
        token = False
        continue
    try:
        nAtual = resp[i]
        nProx = resp[i+1]
        if romanos[nAtual] < romanos[nProx]:
            valor += romanos[nAtual + nProx]
            token = True
            continue
    except:
        valor += romanos[nAtual]
        continue
    valor += romanos[nAtual]

print(valor)