#sistema escalavel é melhor AQUI NAO CONTROLA BOTOES
#https://flet.dev/blog/navigation-and-routing/#page-route  ( Documento  )

from flet import Page,View
from exercicio_de_telas.sistemabancario.main.constructor.constructorCadastrar import ConstructorCadastrar
def start(page:Page):

    page.title="Sistema Bancario"


    def modificarRota(rota):
        page.views.clear() #limpando a tela quando vc trocar
        page.views.append(
            View(
                route="/",
                controls=[
                    ConstructorCadastrar()
                ]
            )
        )

        #aqui estou entrando em outra pagina
        if page.route=="operacoes":
            page.views.append(
                View(
                    route="operacoes",
                    controls=[
                        ConstructorCadastrar()
                    ]
                )
            )

        page.update() #atualizando para outro pagina

    page.on_route_change=modificarRota    #quando a rota muda faz algo
    page.go(page.route) # isso faz a pagina ir para os ligares