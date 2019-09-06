from itertools import repeat


def multiplica(a, b):
    try:
        floatValue1 = float(a); floatValue2 = float(b)        
        return floatValue1 / (1 / floatValue2)
    except ValueError:
        try:
            float(a)
            repeteString = str(list(repeat(b, int(a))))
            return removeCaractere(repeteString)
        except ValueError:
            float(b)
            repeteString = str(list(repeat(a, int(b))))
            return removeCaractere(repeteString)


def aplicacao():
    valor1 = input('Digite o multiplicador: ')
    valor2 = input('Digite o multiplicando: ')
    result = multiplica(valor1, valor2)
    print(f'{valor1} x {valor2} = {result}')


def removeCaractere(textoCorrigido):
    caractereEspecial1 = str.replace(textoCorrigido, '[', '')
    caractereEspecial2 = str.replace(caractereEspecial1, ']', '')
    caractereEspecial3 = str.replace(caractereEspecial2, ',', '')
    corrigido = str.replace(caractereEspecial3, "'", "")
    return corrigido

aplicacao()




