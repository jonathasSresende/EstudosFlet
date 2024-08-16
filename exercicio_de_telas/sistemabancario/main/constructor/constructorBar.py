from exercicio_de_telas.sistemabancario.views.viewBar import ViewBar
from exercicio_de_telas.sistemabancario.controller.controllerBar import ControllerBarMenu
def constructorBar():
    barraOpcoes=ViewBar()
    controllerBar=ControllerBarMenu(barraOpcoes)

    return barraOpcoes