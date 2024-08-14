from  flet import (UserControl,Image,TextField,
                   ElevatedButton,ResponsiveRow,
                   Column,MainAxisAlignment,Text,FontWeight,Row,
                   icons,ButtonStyle,MaterialState,RoundedRectangleBorder,
                   AlertDialog,DataTable,DataColumn,DataCell,DataRow)

from exercicio_de_telas.sistemabancario.utils.paletaCores import CoresAplicacao
class ViewOperacoes(UserControl):
    def __init__(self):
        super().__init__()
        self.cores=CoresAplicacao()

        self.gif_banner=Image(src="tela.png")
        self.btn_depositar=ElevatedButton(text="DEPOSITAR",
                                          style=ButtonStyle(color=self.cores.corBranca,
                                                            bgcolor={
                                                                MaterialState.DEFAULT:self.cores.corDefault
                                                            },
                                                            shape=RoundedRectangleBorder(radius=5)
                                                            ),width=400,height=350)
        self.btn_sacar = ElevatedButton(text="SACAR",
                                            style=ButtonStyle(color=self.cores.corBranca,
                                                              bgcolor={
                                                                  MaterialState.DEFAULT: self.cores.corDefault
                                                              },
                                                              shape=RoundedRectangleBorder(radius=5)
                                                              ), width=400, height=350)
        self.t_field_deposita = AlertDialog ("Você deseja Depositar?")
        self.t_field_sacar = AlertDialog ("Você deseja Sacar?")
        # self.t_field_tabela=DataTable(
        #     columns=[
        #         DataColumn(DataTable.Text("Login")),
        #         DataColumn(DataTable.Text("Email")),
        #         DataColumn(DataTable.Text("Telefone")),
        #         DataColumn(DataTable.Text("Operação")),
        #         DataColumn(DataTable.Text("Saldo")),
        #     ],
        #     rows=[
        #         DataRow(
        #             cells=[
        #                 DataCell(Text("**********")),
        #                 DataCell(Text("**********")),
        #                 DataCell(Text("**********")),
        #             ],
        #         ),
        #         DataRow(
        #             cells=[
        #                 DataCell(Text("**********")),
        #                 DataCell(Text("**********")),
        #                 DataCell(Text("**********")),
        #             ],
        #         ),
        #         DataRow(
        #             cells=[
        #                 DataCell(Text("**********")),
        #                 DataCell(Text("**********")),
        #                 DataCell(Text("**********")),
        #             ],
        #         ),
        #     ],
        # )

    def build(self):
        linha1=ResponsiveRow(controls=[
            Column(col={"xs":12,"sm":10,"md":4,"lg":2},controls=[self.gif_banner])
        ],alignment=MainAxisAlignment.CENTER)
        linha2=ResponsiveRow(controls=[
            Column(col={"xs":12,"sm":10,"md":4,"lg":3},controls=[self.btn_depositar])
        ],alignment=MainAxisAlignment.CENTER)
        linha3=ResponsiveRow(controls=[
        Column(col={"xs": 12, "sm": 10, "md": 4, "lg": 3}, controls=[self.btn_sacar])
        ],alignment=MainAxisAlignment.CENTER)

        return Column(controls=[
            linha1,linha2,linha3
        ])

