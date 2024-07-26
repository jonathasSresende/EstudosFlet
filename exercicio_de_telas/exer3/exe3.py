from flet import *

#USANDO LIPAR TELA
# def main (pagina:Page):
#     pagina.title="Tela de senha"
#     pagina.window_max_width=340
#     pagina.window_max_height=640
#
#     pagina.window_height=640
#     pagina.window_width=340
#
#     pagina.window.center()
#
#     pagina.bgcolor = ""
#
#     t_field_login= TextField(label="Login")
#     t_field_senha= TextField(label="senha",password=True)
#
#     btn_entrar=ElevatedButton(text="Entrar")
#
#     def login (e):
#         if t_field_login.value == "user" and t_field_senha.value == "123":
#             pagina.clean()
#             pagina.add(Text("Bemvindo"))
#             pagina.update()
#         else:
#             pagina.add(Text("Senha incorreta"))
#             pagina.update()
#
#     btn_entrar.on_click=login
#
#     txt_resposta=Text(value="",size=40)
#
#
#     pagina.add(t_field_login)
#     pagina.add(t_field_senha)
#     pagina.add(btn_entrar)
#     pagina.add(txt_resposta)
#
#     pagina.update()
#
# app(target=main)

#Estou criando uma paleta de cores e dando as nomes para elas para usar mais facil
colorPrimary="#013A40"
secondeColor="#04D9D9"
colorBar="#038C8C"
fontColor="#FFFAFA"
colorTeste="#D93636"
backgroundColor="#04D9D9"

def main (pagina:Page):
    pagina.title="Tela de senha"
    imajao=Image(src="aaaaaaaaaaaa.png", width=200, height=200)
    pagina.window_max_width=600
    pagina.window_max_height=600

    pagina.window_height=600
    pagina.window_width=600

    pagina.window.center()

    pagina.bgcolor = colorPrimary
#                                          icon ser para editar na sua tela tem como copias no site https://flet.dev/gallery ou importa com (.)
    t_field_login= TextField(label="Login",icon=icons.LOGIN,color="#FFFAFA")
    t_field_senha= TextField(label="senha",icon=icons.PASSWORD,password=True,color="#FFFAFA")
#                                           TAMANHO
    btn_entrar=ElevatedButton(text="Entrar",width=280,
#                             Formataçao do click do botao
                              style=ButtonStyle(
                                  shape=RoundedRectangleBorder(radius=0),
                                  bgcolor={

                                      MaterialState.DEFAULT:colorBar,
                                      MaterialState.HOVERED:secondeColor
                                  },
                                  color=fontColor
                                 ))
    lineImg= Row(controls=[imajao],alignment=MainAxisAlignment.CENTER)
    line1 = Row(controls=[t_field_login],alignment=MainAxisAlignment.CENTER)
    line2 = Row(controls=[t_field_senha],alignment=MainAxisAlignment.CENTER)
    line3 = Row(controls=[btn_entrar],alignment=MainAxisAlignment.CENTER)
    coluna = Column(controls=[lineImg,line1,line2,line3])
    #o controls dentro do column tem q ser uma lista[]
    #coluna=Column(controls=[t_field_login,t_field_senha,btn_entrar])

    #controls permite q eu trabalhe com mais de um contender
    #pagina.add(t_field_login,t_field_senha,btn_entrar)
    pagina.add(coluna)

    pagina.update()

if __name__ == '__main__':

    app(target=main)

