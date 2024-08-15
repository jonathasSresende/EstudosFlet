from exercicio_de_telas.sistemabancario.views.viewCadastro import ViewCadastro
from exercicio_de_telas.sistemabancario.controller.controllerCadastrar import ControllerCadastrar
def ConstructorCadastrar():
    telaCadastro=ViewCadastro()
    controllerCadastrar=ControllerCadastrar(telaCadastro)
    return telaCadastro