nota = float(input('nota: '))
freq = float(input('freq: '))
if freq <75:
    print('Reprovado por falta')
elif nota >=7:
    print('aprovado')
elif nota>=5:
    print('AF')
else:
    print('reprovado')