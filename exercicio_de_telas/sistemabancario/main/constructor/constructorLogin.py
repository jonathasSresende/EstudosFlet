from exercicio_de_telas.sistemabancario.views.viewLogin import ViewLogin
from exercicio_de_telas.sistemabancario.controller.controllerLogin import ControllerLogin
def ConstructorLogin():
    telaLogin=ViewLogin()
    controllerLogin=ControllerLogin(telaLogin)

    return telaLogin