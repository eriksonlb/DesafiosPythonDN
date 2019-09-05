def multiplica_sem_loop(a,b)
    return a / (1 / b)

    valor1 = int(input('Digite o multiplicador: '))
    valor2 = int(input('Digite o multiplicando: '))
    result = multiplica_sem_loop(valor1, valor2)
    print(f'{valor1} x {valor2} = {result}')
