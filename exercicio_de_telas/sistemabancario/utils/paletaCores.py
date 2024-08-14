

class CoresAplicacao:

    def __init__(self)->None:
        self.__corPrimaira:str="#1b9b85"
        self.__corSecudaria:str="#136f5f"
        self.__corHover:str="#1b9b85"
        self.__corDefault:str="#27debf"
        self.__corBranca:str="#ffffff"

    @property
    def corPrimaria(self)->str:
        """
        Constante para retornar a cor primaria
        :return: str
        """
        return self.__corPrimaira

    @property
    def corSecundaria(self)->str:
        """
        Constante para retornar a cor secundaria
        :return: str
        """
        return self.__corSecudaria

    @property
    def corHouver(self)->str:
        """
        Constante para retornar a cor hover dos botões
       :return: str
        """
        return self.__corHover

    @property
    def corDefault(self)->str:
        """
        Constante para retornar a cor Default
        :return: str
        """
        return self.__corDefault

    @property
    def corBranca(self) -> str:
        """
        Constante para retornar a cor branca
        :return: str
        """
        return self.__corBranca
