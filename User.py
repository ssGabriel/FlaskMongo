

class User:
    def __init__(self, user_name,password):
        self.user_name = user_name
        self.password = password

    def autentificar(self,senha, dc):
        if dc["password"] == senha:
            return True
        return False

    def getUserMongo(self):
        return {"user_name":self.user_name }