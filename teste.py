def converterParaBinario(n):
    numeroBinario = bin(n)
    return str(bin(n)[2:].zfill(8))


# def soma(a, b):
#     valor1 = a & b
#     valor2 = valor1 << 1
#     valor3 = a ^ b
#     valor4 = valor2 ^ valor3
#     return valor4



v1 = int(input ('Digite o primeiro valor: '))
v2 = int(input ('Digite o segundo valor: '))

v1Binario = converterParaBinario(v1)
v2Binario = converterParaBinario(v2)

valor1 = v1 & v2
valor2 = valor1 << 1
valor3 = v1 ^ v2
valor4 = valor2 ^ valor3

print(f'{bin(v1)} + {bin(v2)} = {valor4}')
print(f'\n{v1}  --> {v1Binario}\n{v2}   --> {v2Binario}\n')
print(f'\n\n---->  {v1} & {v2} = {valor1}\n\n  {v1Binario}\n  {v2Binario}\n{"_" *20}\n  {converterParaBinario((valor1))}')
print(f'\n\n---->  {valor1} << 1 = {valor2}\n\n  {v1Binario}\n  {converterParaBinario(valor1)}\n{"_" *20}\n  {converterParaBinario((valor2))}')
print(f'\n\n---->  {v1} ^ {v2} = {valor3}\n\n  {v1Binario}\n  {v2Binario}\n{"_" *20}\n  {converterParaBinario(valor3)}')
print(f'\n\n---->  {valor2} ^ {valor3} = {valor4}\n\n  {converterParaBinario(valor2)}\n  {converterParaBinario(valor3)}\n{"_" *20}\n  {converterParaBinario(valor4)}\n')