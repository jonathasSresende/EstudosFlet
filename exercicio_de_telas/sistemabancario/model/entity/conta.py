
class Conta:
    """
    Aqui estamos colocando o saldo da conta como o id da conta e ida do usuario

    """
    def __init__(self,id_conta:int, idUsuario:int, saldo:float)->None:
        self.id_conta=id_conta
        self.idUsuario=idUsuario
        self.saldo=saldo