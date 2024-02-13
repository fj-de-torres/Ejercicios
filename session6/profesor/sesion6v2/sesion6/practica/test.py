
digitos = ['1.5', 'a', '5.5']


numeros =  []
for digito in digitos:
    try:
        numero = float(digito)
        numeros.append(numero)
    except Exception:
        continue

print(numeros)
