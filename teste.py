def converterParaBinario(n):
    numeroBinario = bin(n)
    return numeroBinario


def soma(a, b):
    valor1 = a & b
    valor2 = valor1 << 1
    valor3 = a ^ b
    valor4 = valor2 ^ valor3
    return valor4



v1 = int(input ('Digite o primeiro valor: '))
v2 = int(input ('Digite o segundo valor: '))
print(f'{v1} + {v2} = {soma(v1,v2)}')

# n1 = int(input('Numero: '))
# print(converterParaBinario(n1))

# 4 + 5
# 00000100
# 00000101
# faz um & = temp1
# 

# faz ^ com 4 e 5 = temp2
# << temp2

# faz um ^= com a e b 
