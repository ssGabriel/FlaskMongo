
class Customer:
    def __init__(self,nome, email,telefone):
        self.id = None
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def geraDocumento(self):
        doc = {"id" : self.id,
                "nome" : self.nome,
               "telefone" : self.telefone,
               "email" :  self.email
               }
        return doc
