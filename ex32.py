def verificarNumero(x):
    return 'par' if x % 2 == 0 else 'Impar'

num = int(input('>>>'))
retorno = verificarNumero(num)
print(retorno)
print(verificarNumero(15))
print(verificarNumero(150))
print(verificarNumero(1505))
