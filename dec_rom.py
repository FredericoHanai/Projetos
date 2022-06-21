num = int(input("Digite um numero decimal até 4 algarismos: "))

m = num // 1000
c = (num // 100) % 10
d = (num % 100)//10
u = num % 10

uni = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
dez = ["X", "XX", "XXX", "XL", "X", "LX", "LXX", "LXXX", "XC"]
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
