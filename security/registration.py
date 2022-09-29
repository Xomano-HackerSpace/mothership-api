from security.sessions import Session

class Registration:

    def update(self, login: str, nickname: str, level: int, token: str):
        auth = Session.validate_token(token)
        if  auth != True:
            return auth
        ##Alterar cadastro no banco....
        