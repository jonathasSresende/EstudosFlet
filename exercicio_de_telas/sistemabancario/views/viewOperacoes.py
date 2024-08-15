# from  flet import (UserControl,Image,TextField,
#                    ElevatedButton,ResponsiveRow,
#                    Column,MainAxisAlignment,Text,FontWeight,Row,
#                    icons,ButtonStyle,MaterialState,RoundedRectangleBorder,
#                    AlertDialog,DataTable,DataColumn,DataCell,DataRow)
#
# from exercicio_de_telas.sistemabancario.utils.paletaCores import CoresAplicacao
# class ViewOperacoes(UserControl):
#     def __init__(self):
#         super().__init__()
#         self.cores=CoresAplicacao()
#
#         self.gif_banner=Image(src="tela.png")
#         self.btn_depositar=ElevatedButton(text="DEPOSITAR",
#                                           style=ButtonStyle(color=self.cores.corBranca,
#                                                             bgcolor={
#                                                                 MaterialState.DEFAULT:self.cores.corDefault
#                                                             },
#                                                             shape=RoundedRectangleBorder(radius=5)
#                                                             ),width=200,height=50)
#         self.btn_sacar = ElevatedButton(text="SACAR",
#                                             style=ButtonStyle(color=self.cores.corBranca,
#                                                               bgcolor={
#                                                                   MaterialState.DEFAULT: self.cores.corDefault
#                                                               },
#                                                               shape=RoundedRectangleBorder(radius=5)
#                                                               ), width=200, height=50)
#         self.t_field_deposita = AlertDialog ("Você deseja Depositar?")
#         self.t_field_sacar = AlertDialog ("Você deseja Sacar?")
#         self.t_field_tabela=DataTable(
#             columns=[
#                 DataColumn(DataTable.Text("Login")),
#                 DataColumn(DataTable.Text("Email")),
#                 DataColumn(DataTable.Text("Telefone")),
#                 DataColumn(DataTable.Text("Operação")),
#                 DataColumn(DataTable.Text("Saldo")),
#             ],
#             rows=[
#                 DataRow(
#                     cells=[
#                         DataCell(Text("**********")),
#                         DataCell(Text("**********")),
#                         DataCell(Text("**********")),
#                     ],
#                 ),
#                 DataRow(
#                     cells=[
#                         DataCell(Text("**********")),
#                         DataCell(Text("**********")),
#                         DataCell(Text("**********")),
#                     ],
#                 ),
#                 DataRow(
#                     cells=[
#                         DataCell(Text("**********")),
#                         DataCell(Text("**********")),
#                         DataCell(Text("**********")),
#                     ],
#                 ),
#             ],
#         )
#
#     def build(self):
#         linha1=ResponsiveRow(controls=[
#             Column(col={"xs":12,"sm":10,"md":4,"lg":2},controls=[self.gif_banner])
#         ],alignment=MainAxisAlignment.CENTER)
#         linha2=ResponsiveRow(controls=[
#             Column(col={"xs":12,"sm":10,"md":4,"lg":3},controls=[self.btn_depositar,self.btn_sacar])
#         ],alignment=MainAxisAlignment.CENTER)
#
#
#         return Column(controls=[
#             linha1,linha2
#         ])



from flet import (UserControl,Image,TextField,
                    ElevatedButton,ResponsiveRow,
                    Column,MainAxisAlignment,Text,FontWeight,Row,
                    icons,ButtonStyle,MaterialState,RoundedRectangleBorder,
                    AlertDialog,DataTable,DataColumn,DataCell,DataRow)

from exercicio_de_telas.sistemabancario.utils.paletaCores import CoresAplicacao

class ViewOperacoes(UserControl):

    def __init__(self):
        super().__init__()
        self.cores=CoresAplicacao()
        self.img_operacoes=Image(src="Banner_jonathas.gif")
        self.btnDepositar=ElevatedButton(text="Depositar",
                                         style=ButtonStyle(
                                             color=self.cores.corBranca,
                                             bgcolor={
                                                 MaterialState.DEFAULT: self.cores.corDefault,
                                                 MaterialState.HOVERED: self.cores.corSecundaria
                                             },
                                             shape=RoundedRectangleBorder(radius=5),

                                         ),width=200,height=45)
        self.btnSacar=ElevatedButton(text="Sacar",
                                     style=ButtonStyle(
                                             color=self.cores.corBranca,
                                             bgcolor={
                                                 MaterialState.DEFAULT: self.cores.corDefault,
                                                 MaterialState.HOVERED: self.cores.corSecundaria
                                             },
                                             shape=RoundedRectangleBorder(radius=5),

                                         ),
                                     width=200,height=45)
        self.t_field_valor=TextField(label="Valor")

        self.tabela=DataTable(
            expand=True,
            columns=[
                DataColumn(label=Text("Login", color=self.cores.corPrimaria)),
                DataColumn(label=Text("Email",color=self.cores.corPrimaria)),
                DataColumn(label=Text("Tel",color=self.cores.corPrimaria)),
                DataColumn(label=Text("Operação",color=self.cores.corPrimaria)),
                DataColumn(label=Text("Saldo",color=self.cores.corPrimaria))

            ]
        )

    def build(self):

        lineIMG=ResponsiveRow(controls=[
            Column(controls=[self.img_operacoes])],alignment=MainAxisAlignment.CENTER)

        line2=ResponsiveRow(controls=[
            Column(col={"xs":12,"sm":10,"md":4,"lg":4},controls=[
                self.btnSacar,
                self.btnDepositar
            ]),
            Column(col={"xs":12,"sm":10,"md":8,"lg":6},controls=[
                self.t_field_valor
            ])
        ], alignment=MainAxisAlignment.CENTER)

        return Column(controls=[
            lineIMG,
            Row(controls=[Text("Operações",color=self.cores.corPrimaria,weight=FontWeight.BOLD,
                               size=30),
],alignment=MainAxisAlignment.CENTER),
            line2,
            Row(controls=[self.tabela],alignment=MainAxisAlignment.CENTER)
        ])
