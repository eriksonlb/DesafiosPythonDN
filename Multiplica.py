def multiplica(a, b):
    resultado = 0
    for n in range(a):
        resultado += b
    return resultado


valor1 = int(input('Digite o multiplicador: '))
valor2 = int(input('Digite o multiplicando: '))
result = multiplica(valor1, valor2)
print(f'{valor1} x {valor2} = {result}')


