class cliente:
    def __init__(self,nome,nascimento,sexo,limite,endereco):
        self.nome = nome
        self.nascimento = nascimento
        self.sexo = sexo
        self.limite = limite 
        self.endereco = endereco

    def imprimir(self):
        print(self.nome)
        print(self.nascimento)
        print(self.sexo)
        print(self.limite)
        print(self.endereco)

cliente1 = cliente( "vitoria", "2007","feminino", "10.000", "bairro sao cristovao")        
cliente1. imprimir()
