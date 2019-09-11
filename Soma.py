def soma(a, b):
    return  a - (b * (-1))


valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
print(f'{valor1} + {valor2} =  {soma(valor1, valor2)}')