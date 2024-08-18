#sistema escalavel é melhor AQUI NAO CONTROLA BOTOES
#https://flet.dev/blog/navigation-and-routing/#page-route  ( Documento  )

from flet import Page,View
from exercicio_de_telas.sistemabancario.main.constructor.constructorCadastrar import ConstructorCadastrar
from exercicio_de_telas.sistemabancario.main.constructor.constructorOperacao import ConstructorOperacoes
from exercicio_de_telas.sistemabancario.main.constructor.constructorBar import constructorBar
from exercicio_de_telas.sistemabancario.main.constructor.constructorLogin import ConstructorLogin
from exercicio_de_telas.sistemabancario.main.constructor.constructorRelatorio import ConstructorRelatorio
def start(page:Page):

    page.title="Sistema Bancario"


    def modificarRota(rota):
        page.views.clear() #limpando a tela quando vc trocar
        page.views.append(
            View(
                route="/",
                controls=[
                    ConstructorLogin()


                ],drawer=constructorBar() #PARA ALTERA PARA OUTRO LUGA NOS BOTAO TEM Q USAR O DRAWER
            )
        )

        #aqui estou entrando em outra pagina
        if page.route=="/login":
            page.views.append(
                View(
                    route="login",
                    controls=[
                        constructorBar(),
                        ConstructorLogin()
                    ],drawer=constructorBar()
                )
            )

        if page.route=="/operacoes":
            page.views.append(
                View(
                    route="operacoes",
                    controls=[
                        constructorBar(),
                        ConstructorOperacoes()
                    ],drawer=constructorBar()
                )
            )

        if page.route=="/cadastrar":
            page.views.append(
                View(
                    route="cadastrar",
                    controls=[
                        constructorBar(),
                        ConstructorCadastrar()
                    ],drawer=constructorBar()
                )
            )

        if page.route=="/relatorio":
            page.views.append(
                View(
                    route="relatorio",
                    controls=[
                        constructorBar(),
                        ConstructorRelatorio()
                    ],drawer=constructorBar()
                )
            )




        page.update() #atualizando para outro pagina

    page.on_route_change=modificarRota    #quando a rota muda faz algo
    page.go(page.route) # isso faz a pagina ir para os lugares