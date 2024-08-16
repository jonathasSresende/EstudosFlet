from flet import (UserControl,Text,Image,TextField,ElevatedButton,ButtonStyle,MaterialState,
                  RoundedRectangleBorder,ResponsiveRow,Column,MainAxisAlignment,alignment,Row)


from exercicio_de_telas.sistemabancario.utils.paletaCores import CoresAplicacao
class ViewLogin(UserControl):
    def __init__(self):
        super().__init__()
        self.cores=CoresAplicacao()
        self.titulo=Text("Login",size=30,color=self.cores.corPrimaria)
        self.img_login=Image(src="tela.png")
        self.t_field_login=TextField(label="Login")
        self.t_field_senha=TextField(label="Senha",password=True,can_reveal_password=True) #can_reveal_password= olinho de aparecer ou nao a senha
        self.btn_entrar=ElevatedButton(text="Entrar",
                                       style=ButtonStyle(color=self.cores.corBranca,
                                                                bgcolor={
                                                                    MaterialState.DEFAULT:self.cores.corDefault
                                                                },shape=RoundedRectangleBorder(radius=10)

                                                                ))


    def build(self):
        linhaBtnEntrar=Row(col={"xs":6,"sm":2,"md":3,},
                           controls=[self.btn_entrar])

        linhaImg=Row(controls=[self.img_login],alignment=MainAxisAlignment.CENTER)

        layout=ResponsiveRow(
            controls=[
                Column( col={"xs":10,"sm":8,"md":6,"lg":5,"xl":3},                          #esse vai ser padrao por exem: usaer uma linha e uma coluna dentro para modificar tudo
                    controls=[

                        #aqui dentro colar as nossas coisas!!!!!
                        Column(col={"xs":6,"sm":2,"md":1,"lg":2,"xl":1},controls=[linhaImg],alignment=alignment.center),  #coluna da img

                        Column(col={"xs":10,"sm":8,"md":6,"lg":5,"xl":3},controls=[self.titulo,                                 #coluna dos conteudos
                                                                                   self.t_field_login,
                                                                                   self.t_field_senha,
                                                                                   linhaBtnEntrar
                                                                                   ]) #fim da coluna do campo de botoes


                    ],alignment=MainAxisAlignment.CENTER
                ) #fim da coluna principal
            ],alignment=MainAxisAlignment.CENTER
        )#fim da linha Principal


        return layout