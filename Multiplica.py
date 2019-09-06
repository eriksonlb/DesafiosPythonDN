"esta dando erro porque os dados estão vindo como string. thing about it"
def multiplica(a, b):
    resultado = None
    if type(a) == str or type(b) == str:
        if type(a) == str:
            for n in range(b):
                resultado += a
            return resultado
        else:
            for n in range(a):
                resultado += b
            return resultado
    else:
        return a / (1 / b)


valor1 = input('Digite o multiplicador: ')
valor2 = input('Digite o multiplicando: ')
result = multiplica(valor1, valor2)
print(f'{valor1} x {valor2} = {result}')


