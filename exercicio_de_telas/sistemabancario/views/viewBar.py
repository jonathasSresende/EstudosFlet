from  flet import  Container,AppBar,IconButton,icons,PopupMenuButton,PopupMenuItem,Image

from exercicio_de_telas.sistemabancario.utils.paletaCores import CoresAplicacao
class ViewBar(AppBar):
    def __init__(self):
        super().__init__()
        self.cores=CoresAplicacao()
        self.logo=Image(src="logo11.png")
        self.btnCadastrar=PopupMenuItem(icon=icons.ASSIGNMENT_IND, text="Cadastrar")
        self.btnOperacoes=PopupMenuItem(icon=icons.PRICE_CHECK_ROUNDED, text="Operações")
        self.btnRelatorio=PopupMenuItem(icon=icons.AREA_CHART_OUTLINED, text="Relatório")

        self.menu=PopupMenuButton(                  #esse serve para criar o botao 3 potinho q qndo clicar ele abre as coisas dentro
            items=[
                self.btnCadastrar,
                self.btnOperacoes,
                self.btnRelatorio
                ]
        )
        self.btnVoltar=IconButton(icon=icons.LOGOUT,
                                   icon_color=self.cores.corPrimaria)

        self.leading=self.btnVoltar
        self.title=self.logo
        self.center_title=True
        self.actions=[self.menu]
