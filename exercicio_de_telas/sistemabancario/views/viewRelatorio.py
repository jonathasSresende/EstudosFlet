from flet import (UserControl,Text,Image,TextField,ElevatedButton,ButtonStyle,MaterialState,
                  RoundedRectangleBorder,ResponsiveRow,Column,MainAxisAlignment,alignment,Row,FontWeight)
from exercicio_de_telas.sistemabancario.utils.paletaCores import CoresAplicacao
class ViewRelatorio(UserControl):
    def __init__(self):
        super().__init__()
        self.cores=CoresAplicacao()
        self.imgGrafico=Image(src="Grafico.png")
        self.btnGrafico=ElevatedButton(text="Gráfico",
                                       style=ButtonStyle(color=self.cores.corBranca,
                                                                bgcolor={
                                                                    MaterialState.DEFAULT:self.cores.corDefault
                                                                },shape=RoundedRectangleBorder(radius=10)
                                                                ))
        self.statusRelatorio=Text("Carlos Silva Carvalho,R$: 10.000,00",color=self.cores.corPrimaria,weight=FontWeight.BOLD,
                               size=30)
        self.btnRelatorio=ElevatedButton(text="Gráfico",
                                            style=ButtonStyle(
                                                color=self.cores.corBranca,
                                                bgcolor={
                                                MaterialState.DEFAULT:self.cores.corDefault,
                                                MaterialState.HOVERED:self.cores.corSecundaria
                                                },shape=RoundedRectangleBorder(radius=10)
                                            ),width=200, height=45
                                        )

    def build(self):
        #linhaDosBotoes=Row(col={"xs":6,"sm":2,"md":3,},controls=[self.statusRelatorio,self.btnGrafico],alignment=MainAxisAlignment.END)
        linhaDaImagemGrafico=Row(controls=[self.imgGrafico],alignment=MainAxisAlignment.CENTER)

        layout=ResponsiveRow(
            controls=[
                Column(col={"xs":10,"sm":8,"md":6,"lg":5,"xl":3},
                       controls=[


                           Column(col={"xs":10,"sm":8,"md":6,"lg":5,"xl":3}, controls=[self.btnGrafico]),

                           Column(col={"xs":10,"sm":8,"md":6,"lg":5,"xl":3},controls=[self.statusRelatorio]),

                           Column(col={"xs": 6, "sm": 2, "md": 1, "lg": 2, "xl": 1}, controls=[linhaDaImagemGrafico],
                                  alignment=MainAxisAlignment.CENTER),




                       ],alignment=MainAxisAlignment.CENTER
                )
            ]
        )

        return layout

