#Strings

celular = "(41)96574-1728"

x = celular.find('(') + 1
y = celular.find(')')

indiceInicialCodigoArea = x
indiceFinalCodigoArea   = y

print(x,y)
print (celular[indiceInicialCodigoArea:indiceFinalCodigoArea])

from Aula5Classe import ExtratorArgumentoURL

argumentos = ExtratorArgumentoURL('dasas')

moedas = argumentos.retornaMoedas()
print(moedas)