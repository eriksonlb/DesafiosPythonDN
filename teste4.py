def fatorial(n):
    if n == 1:
        return n
    a = fatorial(n - 1) * n
    return ('Fatorial(' + str(n) + ' - 1) * ' + str(n) + '\n    >> fatorial(' + str((n - 1)) + ') * ' + str(n) + ' = ' + str(a) + '\n\n')


def fibonacci(n):
    if n <= 1:
        return n
    else:  
        return str(fibonacci(n-1)) + ' + ' + str(fibonacci(n-2)) + '\n'
        

escolha = int(input('[1] - Fatorial \n[2] - Fibonacci\n\n'))
if escolha == 1:
    valorFatorial = int(input('Valor: '))
    print(fatorial(valorFatorial))
elif escolha == 2:
    limiteFibonacci = int(input('Limite: '))
    print(fibonacci(limiteFibonacci))