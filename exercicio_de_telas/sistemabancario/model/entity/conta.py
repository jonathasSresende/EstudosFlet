
class Conta:
    """
    Aqui estamos colocando o saldo da conta como o id da conta e ida do usuario

    """
    def __init__(self,id_conta:int, idUsuario:int, saldo:float)->None:
        self.id_conta=id_conta
        self.idUsuario=idUsuario
        self.saldo=saldo


    def sacar(self,valor:float)->bool:
        """
        Esse metodo vai descrementar valores da variavel saldo
        :param valor: float
        :return: boll
        """

        if valor>=self.saldo:
            self.saldo-=valor
            return True
        else:

            return False

    def depositar(self,valor:float)->bool:
        """
        Esse metodo vai adcionar valores na variavel saldo
        :param valor: float
        :return: bool
        """

        self.saldo+=valor
        return True


