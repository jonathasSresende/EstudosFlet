from flet import *

def main (page:Page):
    page.title="Trbalhando com Container"
    container1=Container(
        content=Text("sei la",size=23,weight=FontWeight.W_600,color=colors.BLACK),
        bgcolor=colors.BLUE,
        width=200,
        height=200,

        #padding=45         Sao 3 tipos de padding para usar
        #padding=padding.symmetric(vertical=80,horizontal=50)
        padding=padding.only(top=150,left=90),

        #border=border.all(width=5,color=colors.BLACK)          border é para criar bordas do contender
        border=border.only(top=BorderSide(5,color=colors.BLACK),bottom=BorderSide(15,color=colors.BLACK)),

        margin=margin.all(40), #margin é para vc mover ele na tela
        #margin=margin.only(top=200)
        #margin=margin.symmetric(horizontal=50,vertical=500)

        #gradient=LinearGradient(begin=alignment.top_center,end=alignment.bottom_center,colors=[colors.BLUE,colors.CYAN_900]), #para fazer o contender degrade
        #border_radius=border_radius.all(40),
        border_radius=border_radius.only(top_left=15,top_right=15 , bottom_left=15),
        image_src="aaaaaaaaaaaa.png",
        shadow=BoxShadow(spread_radius=1,blur_radius=15,color=colors.BLUE,offset=Offset(0,0),blur_style=ShadowBlurStyle.OUTER),
    #spread_radius é para borda começar fica degrade,,,,blur_radius é para desfocar,,,,offset trabalha com x e y ,,,,,,blur_style dexiar mais tramparencia ou mais solida .OUTER, .SOLID, .NORMAL
        #alignment=Alignment(-1,0) #trabalha com o alinhamento x e y centro 0
    )
    line1=Row(controls=[container1,container1])
    coluna=Column(controls=[line1])


    page.add(coluna)
    page.update()

if __name__ == '__main__':
    app(target=main)