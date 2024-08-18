from exercicio_de_telas.sistemabancario.views.viewBar import ViewBar

class ControllerBarMenu:
    def __init__(self,viewBar:ViewBar)->None:
        self.barraMenu=viewBar
        self.voltar=viewBar.btnVoltar
        self.btnCadastrar = viewBar.btnCadastrar
        self.btnOperacoes=viewBar.btnOperacoes
        self.btnRelatorio=viewBar.btnRelatorio


        self.btnOperacoes.on_click=self.trocarDePagina_Operacoes
        self.btnCadastrar.on_click=self.trocarDePagina_Cadastrar
        self.barraMenu.btnVoltar.on_click=self.trocarDePagina_botaoVoltar
        self.btnRelatorio.on_click=self.trocaDePagina_Relatorio
    def trocarDePagina_Operacoes(self,e):
        self.barraMenu.page.go("/operacoes")

    def trocarDePagina_Cadastrar(self,e):
        self.barraMenu.page.go("/cadastrar")

    def trocarDePagina_botaoVoltar(self,e):
        self.barraMenu.page.go("/login")

    def trocaDePagina_Relatorio(self,e):
        self.barraMenu.page.go("/relatorio")