class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return super().__str__() + f' - Duração: {self.duracao}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):
        return super().__str__() + f' - Temporadas: {self.temporadas}'

#class PlayList(list):
#    def __init__(self, nome, programas):
#        self.nome = nome
#       super().__init__(programas)

class PlayList:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2)
atlanta.nome = 'atlanta'
atlanta.dar_like()
atlanta.dar_like()

programas = [vingadores, atlanta]
playlist = PlayList('PlayList1',programas)
for programa in playlist:
    print(programa)

print(len(playlist))