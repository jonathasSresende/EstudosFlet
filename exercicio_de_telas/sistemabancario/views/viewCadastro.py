#pagina burro so serve para ver o a tela


from  flet import (UserControl,Image,TextField,
                   ElevatedButton,ResponsiveRow,
                   Column,MainAxisAlignment)

class ViewCadastro(UserControl):
        def __init__(self):
            super().__init__()

            self.img_cadastro=Image(src="tela.png")
            self.t_field_login=TextField(label="Login")
            self.t_field_senha=TextField(label="Senha",password=True)
            self.t_field_email=TextField(label="Email")
            self.t_field_telefone=TextField(label="Telefone")
            self.t_field_saldo=TextField(label="Saldo",prefix_text="R$")
            self.btn_cadastrar=ElevatedButton(text="Cadastrar")

        def build(self):

            linha1=ResponsiveRow(controls=[
                Column(col={"xs":12,"sm":10,"md":4,"lg":2},controls=[self.img_cadastro])
            ],alignment=MainAxisAlignment.CENTER) #final da linha 1

            linha2=ResponsiveRow(controls=[                                                      #sm celular / md Site
                Column(col={"sm":8,"md":2},controls=[self.t_field_login]),                #os col={"sm":8,"md":8}, é o tamanho das colunas
                Column(col={"sm":8,"md":2},controls=[self.t_field_senha]),
                Column(col={"sm":8,"md":2},controls=[self.t_field_email]),
                Column(col={"sm":8,"md":2},controls=[self.t_field_telefone]),
                Column(col={"sm":8,"md":2},controls=[self.t_field_saldo])
            ],alignment=MainAxisAlignment.CENTER) #final da linha 2

            linha3=ResponsiveRow(controls=[
                Column(controls=[self.btn_cadastrar])
            ],alignment=MainAxisAlignment.CENTER) #final da linha 3



            return Column(controls=[
                linha1,linha2,linha3
            ])