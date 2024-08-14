#pagina burro so serve para ver o a tela


from  flet import (UserControl,Image,TextField,
                   ElevatedButton,ResponsiveRow,
                   Column,MainAxisAlignment,Text,FontWeight,Row,
                   icons,ButtonStyle,MaterialState,RoundedRectangleBorder)

from exercicio_de_telas.sistemabancario.utils.paletaCores import CoresAplicacao

class ViewCadastro(UserControl):
        def __init__(self):
            super().__init__()
            self.cores=CoresAplicacao() #tenho que criar esse para usar as cores sem ()

            self.img_cadastro=Image(src="tela.png")
            self.titulo=Text("Cadastrar",size=30,weight=FontWeight.BOLD,color=self.cores.corPrimaria)
            self.t_field_login=TextField(label="Login",icon=icons.LOGIN)                                 #todo t_field tem um icon
            self.t_field_senha=TextField(label="Senha",password=True,icon=icons.PASSWORD)
            self.t_field_email=TextField(label="Email",icon=icons.EMAIL)
            self.t_field_telefone=TextField(label="Telefone",icon=icons.LOCAL_PHONE_SHARP)
            self.t_field_saldo=TextField(label="Saldo",prefix_text="R$",icon=icons.ATTACH_MONEY)
            self.btn_cadastrar=ElevatedButton(text="Cadastrar",
                                              style=ButtonStyle(color=self.cores.corBranca,
                                                                bgcolor={
                                                                    MaterialState.DEFAULT:self.cores.corDefault
                                                                },
                                                                shape=RoundedRectangleBorder(radius=10)

                                                                ),width=200,height=45)

        def build(self):

            linha1=ResponsiveRow(controls=[
                Column(col={"xs":12,"sm":10,"md":4,"lg":2},controls=[self.img_cadastro])
            ],alignment=MainAxisAlignment.CENTER) #final da linha 1

            linhaTitulo=Row(controls=[self.titulo],alignment=MainAxisAlignment.CENTER)

            linha2=ResponsiveRow(controls=[                                                      #sm celular / md Site
                Column(col={"xs":12,"sm":10,"md":4,"lg":4},controls=[self.t_field_login]),                #os col={"sm":8,"md":8}, é o tamanho das colunas
                Column(col={"xs":12,"sm":10,"md":4,"lg":4},controls=[self.t_field_senha]),
                Column(col={"xs": 12, "sm": 10, "md": 4, "lg": 4}, controls=[self.t_field_saldo]),
                Column(col={"xs":12,"sm":10,"md":4,"lg":5},controls=[self.t_field_email]),
                Column(col={"xs":12,"sm":10,"md":4,"lg":4},controls=[self.t_field_telefone]),
                Column(col={"xs":12,"sm":10,"md":4,"lg":3},controls=[self.btn_cadastrar])
            ],alignment=MainAxisAlignment.CENTER) #final da linha 2

            #linha3=ResponsiveRow(controls=[
            #    Column(controls=[self.btn_cadastrar])
            #],alignment=MainAxisAlignment.CENTER) #final da linha 3



            return Column(controls=[
                linha1,linhaTitulo,linha2,#linha3
            ])