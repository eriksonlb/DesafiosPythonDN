from random import randint
import time

def relatorioErro(valor1, valor2, calcError):
    if valor1 < 0 and valor2 < 0 and valor1 % 2 != 0 and valor2 % 2 != 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  negativo impar e negativo impar')
    if valor1 < 0 and valor2 < 0 and valor1 % 2 == 0 and valor2 % 2 == 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  negativo par e negativo par')
    if valor1 < 0 and valor2 < 0 and valor1 % 2 != 0 and valor2 % 2 == 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  negativo impar e negativo par')
    if valor1 < 0 and valor2 < 0 and valor1 % 2 == 0 and valor2 % 2 != 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  negativo par e negativo impar') #negativos 
    if valor1 >= 0 and valor2 >= 0 and valor1 % 2 != 0 and valor2 % 2 != 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  positivo impar e positivo impar')
    if valor1 >= 0 and valor2 >= 0 and valor1 % 2 == 0 and valor2 % 2 == 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  positivo par e positivo par')
    if valor1 >= 0 and valor2 >= 0 and valor1 % 2 != 0 and valor2 % 2 == 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  positivo impar e positivo par')
    if valor1 >= 0 and valor2 >= 0 and valor1 % 2 == 0 and valor2 % 2 != 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  positivo par e positivo impar') #positivo 
    if valor1 >= 0 and valor2 < 0 and valor1 % 2 != 0 and valor2 % 2 != 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  positivo impar e negativo impar')
    if valor1 >= 0 and valor2 < 0 and valor1 % 2 == 0 and valor2 % 2 == 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  positivo par e negativo par')
    if valor1 >= 0 and valor2 < 0 and valor1 % 2 != 0 and valor2 % 2 == 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  positivo impar e negativo par')
    if valor1 >= 0 and valor2 < 0 and valor1 % 2 == 0 and valor2 % 2 != 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  positivo par e negativo impar') #negativos 
    if valor1 < 0 and valor2 >= 0 and valor1 % 2 != 0 and valor2 % 2 != 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  negativo impar e positivo impar')
    if valor1 < 0 and valor2 >= 0 and valor1 % 2 == 0 and valor2 % 2 == 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  negativo par e positivo par')
    if valor1 < 0 and valor2 >= 0 and valor1 % 2 != 0 and valor2 % 2 == 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  negativo impar e positivo par')
    if valor1 < 0 and valor2 >= 0 and valor1 % 2 == 0 and valor2 % 2 != 0:            
        calcError.append(str(valor1) + ' + ' + str(valor2) + '  --  negativo par e positivo impar')


def soma(v1, v2):
    a = v1 
    b = v2
    if (v1 < 0 or v2 < 0) and abs(a) == abs(b):
        return 0
    else:       
        try:
            return a if b == 0 else soma(a ^ b, (a & b) << 1) if a < 0 else soma(b ^ a, (b & a) << 1)
        except Exception:
            a = ~v1
            b = ~v2
            try:
                resultado =  a if b == 0 else soma(a ^ b, (a & b) << 1) if a < 0 else soma(b ^ a, (b & a) << 1)
                return resultado * (-1)
            except Exception:
                return 'Erro!'

def somaRandom():
    b = 0
    relatorio = []
    while b < 100000:        
        v1 = randint(-1000000, 1000000)
        v2 = randint(-1000000, 1000000)
        resultado = soma(v1, v2)
        if type(resultado) != str:
            print(f'\n{v1} + {v2} =  ', end="")
            print(resultado)
            print('    Errado!') if resultado != (v1 + v2) else print('    Correto!')
            print('========================\n')
            # time.sleep(0.2)
        else:
            relatorioErro(v1, v2, relatorio)
        b += 1
    print(f'Calculos rejeitados:\n')
    for i in relatorio:
        print(i)


def somaManual():
    valor1 = int(input('Primeiro valor: '))
    valor2 = int(input('Segundo valor: '))
    resultado = soma(valor1, valor2)
    print(f'\n{valor1} + {valor2} =  ', end="")
    print(resultado)

# try:
#     choice = int(input('Tecle 1 para modo Automático\nOu qualquer tecla para modo Manual:  '))
#     somaRandom()
# except Exception:
# 
somaRandom()    

