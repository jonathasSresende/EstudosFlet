from abc import ABC,abstractmethod
from datetime import date

class Poo1(ABC):
        def __init__(self,nome:str="Carlos")->None:
            self.__nome=nome
            self.__oculto=None
            self.__cont=0

        @property
        def nome(self):
            return self.__nome

        @nome.setter
        def nome(self,novoNome:str)->None:
            self.__nome=novoNome

        def contar(self)->int:
            """
            O meto contar soma mais 1 um valor em cada uma de suas chamadas e retorna o valor somado
            :return: int
            """

            self.__cont += 1
            return  self.__cont



        @abstractmethod
        def calcularIdade(self):
            pass




class Poo2(Poo1):
    def __init__(self,nome,salario:float, anoNascimento:int)->None:
        super().__init__(nome)
        self.__salario:float=salario
        self.__anoNascimento=anoNascimento




    @property
    def anoNascimento(self)->int:
        return self.__anoNascimento

    @anoNascimento.setter
    def anoNascimento(self,anoNascimento)->int:
        self.__anoNascimento=anoNascimento

    @property
    def salario(self)->float:
        return self.__salario

    @salario.setter
    def salario(self, salario) -> None:
        self.__salario = salario



    def calcularIdade(self)->int:
        anoatual=date.today().year
        idade=anoatual-self.__anoNascimento
        return idade


if __name__ == '__main__':

    t1=Poo1("Maria")
    print(t1.contar())
    print(t1.contar())
    print(t1.contar())
    print("_______________________")
    tp2=Poo2("tereza",2500)

    print(tp2.salario)
    print(tp2.nome)
    print(tp2.contar())