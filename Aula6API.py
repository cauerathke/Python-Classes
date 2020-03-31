import requests

class BuscaEndereco:
    
    def __init__(self, cep):
        cep = str(cep)
        if(self.valida_cep(cep)):
            self.cep = cep
        else:
            raise ValueError("Cep inválido") 
    
    def __str__(self):
        return self.formart_cep()
    
    def valida_cep(self, cep):
        if(len(cep) == 8):
            return True
        else:
            return False
    
    def formart_cep(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )

cep_objeto = BuscaEndereco("96900000")
print(cep_objeto.acessa_via_cep())

#r = requests.get("https://viacep.com.br/ws/96900000/json")
#print(r.text)