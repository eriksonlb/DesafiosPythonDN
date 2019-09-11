def fatorial(n):
    if n == 1:
        return n
    a = fatorial(n - 1) * n
    return ('Fatorial(' + str(n) + ' - 1' + ') * ' + str(n) + '\n    >> fatorial(' + str((n - 1)) + ') * ' + str(n) + ' = ' + str(a) + '\n\n')
    

print(fatorial(3))