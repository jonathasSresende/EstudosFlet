
class Cliente:
    """
    Aqui estou colocando id clienter ,id contato , login e senha
    """
    def __init__(self,id_cliente:int,id_contato:int,login:str,senha:str)->None:
        self.id_client=id_cliente
        self.id_contato=id_contato
        self.login=login
        self.senha=senha