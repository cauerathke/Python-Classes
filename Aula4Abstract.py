from abc import ABC #abstract base classes

from collections.abc import MutableSequence
#from numbers import Complex

class PlayList(MutableSequence):
    pass

from collections.abc import Sized

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __len__(self):
        return len(self.descricao)

lista = MinhaListagem('dasdas')
print(len(lista))

#Criação de classe abstrata
from abc import ABCMeta, abstractmethod 
class Programa(metaclass = ABCMeta): 
    @abstractmethod 
    def __str__(self): 
        pass