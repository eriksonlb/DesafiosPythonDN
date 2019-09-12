import time


# for i in range(10):
#     a = ~i
#     print(f'~{i} = ' + str(a))
#     time.sleep(1)
a, b = 10000000000, 2
while b <= 10:    
    print(f'  ---  Usando {b}  ---  \n')
    print(f'{b} >> 1 = ' + str(b >> 1))
    print(f'{b} << 1 = ' + str(b << 1))
    print(f'{b} ^ {b*2} = ' + str(b ^ (b*2)))
    print(f'{b} | {b*2} = ' + str(b | (b*2)))
    print(f'~{b} = ' + str(~b))
    print('\n======================\n')
    b += 1
    time.sleep(1)

# for i in range(10):
#     a = ~i
#     print(f'~{i} = ' + str(a))
#     time.sleep(1)

# a >> 3 é o mesmo que dividir a por 2 3 vezes
