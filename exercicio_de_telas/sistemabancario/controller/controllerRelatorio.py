from exercicio_de_telas.sistemabancario.views.viewRelatorio import ViewRelatorio

class ControllerRelatorio:
    def __init__(self,viewRelatorio:ViewRelatorio)->None:
        self.btntrocarGrafico=viewRelatorio.btnGrafico
        self.btntrocarStatus=viewRelatorio.btnRelatorio

        self.btntrocarGrafico.on_click=self.TrocarImg_Grafico
        self.btntrocarStatus.on_click=self.TrocarTxt_Stats

    def TrocarImg_Grafico(self,e):
        self.trocarGrafico.page.go("/relatorio")

    def TrocarTxt_Stats(self,e):
        self.trocarGrafico.page.go("/relatorio")