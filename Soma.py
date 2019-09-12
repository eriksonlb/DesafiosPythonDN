from random import randint
import time

def soma(v1, v2):
    a = v1 
    b = v2       
    try:
        return a if b == 0 else soma(a ^ b, (a & b) << 1) if a < 0 else soma(b ^ a, (b & a) << 1)
    except Exception:
        return '\n' + str(a) + ' = ' + str(bin(a)) + '\n' + str(b) + '=' + str(bin(b))

b = 0
calcError = []
while b < 100:
    # valor1 = int(input('Primeiro valor: '))
    # valor2 = int(input('Segundo valor: '))
    valor1 = randint(-30, 30)
    valor2 = randint(-30, 30)

    resultado = soma(valor1, valor2)
    if type(resultado) != str:
        print(f'\n{valor1} + {valor2} =  ', end="")
        print(resultado)
        print('========================\n')
    else:
        calcError.append(str(valor1) + ' + ' + str(valor2))
    b += 1
print(f'Calculos rejeitados:')
for i in calcError:
    print(i)