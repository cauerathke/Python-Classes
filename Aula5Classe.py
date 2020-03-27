class ExtratorArgumentoURL:
    def __init__(self,url):
        if self.stringEhValida(url):
            self.url = url
        else:
            raise LookupError('“Url inválida”')

    @staticmethod
    def stringEhValida(url):
        if url:
            return True
        else:
            return False

    def retornaMoedas(self):
        buscaMoedaOrigem = "moedaorigem"
        buscaMoedaDestino = "moedadestino"

        inicioSubstringMoedaOrigem = self.encontraIndiceInicioSubstring(buscaMoedaOrigem)
        finalSubstringMoedaOrigem = self.url.find("&")
        moedaOrigem = self.url[inicioSubstringMoedaOrigem:finalSubstringMoedaOrigem]

        inicioSubstringMoedaDestino = self.encontraIndiceInicioSubstring(buscaMoedaDestino)
        finalSubstringMoedaDestino = self.url.find("&valor")
        moedaDestino = self.url[inicioSubstringMoedaDestino:finalSubstringMoedaDestino]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicioSubstring(self, moedaOuValor):
        return self.url.find(moedaOuValor) + len(moedaOuValor) + 1