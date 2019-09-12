def soma(n):
    if len(n) == 1:
        return n[0]
    else:
        return n[0] + soma(n[1:])

lista = [1, 2, 3]

print(soma(lista))