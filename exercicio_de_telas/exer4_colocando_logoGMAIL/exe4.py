from flet import *
colorPrimary="#013A40"
secondeColor="#04D9D9"
colorBar="#038C8C"
fontColor="#FFFAFA"
colorTeste="#D93636"
backgroundColor="#04D9D9"
def main (pagina:Page):
    pagina.title="tela de senha"
    pagina.window_width=600
    pagina.window_height=600

    pagina.window.center()

    pagina.bgcolor=colorPrimary
    img_titulo=Image(src="../exer3/aaaaaaaaaaaa.png", width=200, height=200)
    t_field_login=TextField(label="User",icon=icons.LOGIN)
    t_field_senha=TextField(label="Password",icon=icons.PASSWORD,password=True)
    btn_botao=ElevatedButton(text="Entrar",width=280,
                             style=ButtonStyle(
                                 shape=RoundedRectangleBorder(radius=150),
                                 bgcolor={
                                     MaterialState.DEFAULT:colorBar,
                                     MaterialState.HOVERED:secondeColor
                                 },
                                 color=fontColor
                             ))
    btn_botao1=TextButton(text="Esqueci a senha",width=200,
                              style=ButtonStyle(shape=RoundedRectangleBorder(radius=150),
                                                bgcolor={MaterialState.DEFAULT:colorBar,
                                                         MaterialState.HOVERED:secondeColor},color=fontColor))
    img_Gmail=Image(src="gmail.png", width=50)
    img_Facebook=Image(src="face.png", width=50)

    lineImg_titulo=Row(controls=[img_titulo],alignment=MainAxisAlignment.CENTER)
    line1=Row(controls=[t_field_login],alignment=MainAxisAlignment.CENTER)
    line2=Row(controls=[t_field_senha],alignment=MainAxisAlignment.CENTER)
    line3=Row(controls=[btn_botao],alignment=MainAxisAlignment.CENTER)
    line4=Row(controls=[btn_botao1],alignment=MainAxisAlignment.CENTER)
    line5=Row(controls=[img_Gmail,img_Facebook],alignment=MainAxisAlignment.SPACE_AROUND)

    coluna=Column(controls=[lineImg_titulo,line1,line2,line3,line4,line5])

    pagina.add(coluna)

    pagina.update()

if __name__ == '__main__':

    app(target=main)

