from validate_docbr import CPF


class ValidaCpf:
    def __init__(self, cpf):
        cpf = str(cpf)
        if(self.valida(cpf)):
            self.cpf = cpf
        else:
            raise Exception("Erro")

    def valida(self, cpf):
        validador = CPF()
        return validador.validate(cpf)
        

    def format_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)

    def __str__(self):
        return self.format_cpf()

#cpf = ValidaCpf(111111111)
#print(cpf)
 
#factory
class Documento:
    @staticmethod
    def criar_novo(documento):
        doc_str = str(documento)
        if len(doc_str) == 11:
            return DocCpf(doc_str)
        if len(doc_str) == 14:
            return DocCnpj(doc_str)
        if len(doc_str) == 20:
            return DocQualquer(doc_str)
        raise ValueError('Documento incorreto!')

class DocCpf:
    pass
class DocCnpj:
    pass
class DocQualquer:
    pass

#regex 
import re

padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "eu gosto do numero 12321323331 w[asdka"
resposta = re.findall(padrao, texto)

print(resposta)

# []	Define um range ou um grupo de caracteres	[0-9]; [a-z]; [abc]
# *	Marca nenhuma, uma ou mais ocorrências	sol*
# {}	Quantidade de repetições de uma ocorrência definida	[abc]{5}
# \d	Qualquer número de 0 até 9	\d{3,4}
# \w	Qualquer número de a té 9 letra de a até z ou _	\w{10}
# |	Um ou outro	@$
# ()	Captura e agrupa	(\w{4})