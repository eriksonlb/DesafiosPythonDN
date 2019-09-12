def soma(a, b):
    while b:
        sobra = a & b
        c = a
        d = b
        a ^= b
        b = sobra << 1
    return a,str.replace(bin(c), '0b', ''), str.replace(bin(d), '0b', '')

v1 = int(input ('Digite o primeiro valor: '))
v2 = int(input ('Digite o segundo valor: '))
print(f'{v1} + {v2} = {soma(v1,v2)}')
# print(fatorial(5))