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

cpf = ValidaCpf(111111111)
print(cpf)
 
