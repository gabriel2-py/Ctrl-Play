class Casa():

    
    def __init__(self, Rua, Bairro, CEP):
       self.Rua = Rua
       self.Bairro = Bairro
       self.CEP = CEP

    def enderecoCompleto(self):
     return "Endereço completo: "+self.Rua+ ", "+self.Bairro+ " - CEP: "+ self.CEP
    

casa1 = Casa(Rua="jegue silva lorerenzo", Bairro="jose machado", CEP="133580")

casa2 = Casa(Rua="lorenzo freitas", Bairro ="São Luis", CEP ="125689")

print(casa1.enderecoCompleto())

print(casa2.enderecoCompleto())