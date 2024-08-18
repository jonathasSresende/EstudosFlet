from exercicio_de_telas.sistemabancario.views.viewOperacoes import ViewOperacoes

class ControllerOperacoes:
    def __init__(self,viewOperacoes:ViewOperacoes)->None:
        self.btnRelatorio=viewOperacoes.btnRelatorio

        self.btnRelatorio.on_click=self.TrocarDePagina_Relatorio

    def TrocarDePagina_Relatorio (self,e):
        self.btnRelatorio.page.go("/relatorio")

