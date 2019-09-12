def soma(a, b):
    binA = str.replace(bin(a), "0b", "")
    binB = str.replace(bin(b), "0b", "")
    print(f'\n{a} -> binario = {binA}')
    print(f'{b} -> binario = {binB}')

    valor1 = a & b
    print(f'\n{a} & {b} = {valor1}')
    print(f'Valor&: {binA} & {binB} = {str.replace(bin(valor1), "0b", "")}')
    print('=-=' * 20)

    print(f'\nDeslocar << 1 no Valor&')
    valor2 = valor1 << 1
    print(f'\nValorBitDeslocado = {valor1} << 1 = {valor2}')
    print(f'Em binario fica: {str.replace(bin(valor1), "0b", "")} << 1 = {str.replace(bin(valor2), "0b", "")}')
    print('=-=' * 20)

    print(f'\nXOR com {a} e {b}')
    valor3 = a ^ b
    print(f'\n{a} ^ {b} = {valor3}')
    print(f'Valor^: {binA} ^ {binB} = {str.replace(bin(valor3), "0b", "")}')
    print('=-=' * 20)


    print(f'\nXOR com {valor2} e {valor3}')
    valor4 = valor2 ^ valor3
    binvalor2 = str.replace(bin(valor2), "0b", "")
    binvalor3 = str.replace(bin(valor3), "0b", "")
    print(f'\n{valor2} ^ {valor3} = {valor4}')
    print(f'Valor^: {binvalor2} ^ {binvalor3} = {str.replace(bin(valor4), "0b", "")}')
    print('=-=' * 20)
    print(f'Resultado = {valor4}')



v1 = int(input ('Digite o primeiro valor: '))
v2 = int(input ('Digite o segundo valor: '))
soma(v1,v2)



# 4 + 5
# 00000100
# 00000101
# faz um & = temp1
# 

# faz ^ com 4 e 5 = temp2
# << temp2

# faz um ^= com a e b 
