from  flet import  Container,AppBar,IconButton,icons,PopupMenuButton,PopupMenuItem,Image

from exercicio_de_telas.sistemabancario.utils.paletaCores import CoresAplicacao
class ViewBar(AppBar):
    def __init__(self):
        super().__init__()
        self.cores=CoresAplicacao()
        self.logo=Image(src="logo11.png")
        self.menu=PopupMenuButton(                  #esse serve para criar o botao 3 potinho q qndo clicar ele abre as coisas dentro
            items=[
                PopupMenuItem(icon=icons.ASSIGNMENT_IND,text="Cadastrar"),
                PopupMenuItem(icon=icons.PRICE_CHECK_ROUNDED, text="Operações"),
                PopupMenuItem(icon=icons.AREA_CHART_OUTLINED, text="Relatório")
            ]
        )
        self.btnVoltar=IconButton(icon=icons.ARROW_BACK_IOS_NEW_ROUNDED,
                                   icon_color=self.cores.corPrimaria)

        self.leading=self.btnVoltar
        self.title=self.logo
        self.center_title=True
        self.actions=[self.menu]
