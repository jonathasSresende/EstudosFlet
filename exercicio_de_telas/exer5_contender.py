from flet import *

def main (page:Page):
    page.title="Tinder da laticha"

    contender=Container(
        bgcolor=colors.PINK_50,
        width=200,
        height=250,

        border=border.only(top=BorderSide(5, color=colors.PINK_700), bottom=BorderSide(15, color=colors.PINK_700)),
        margin=margin.all(40),  # margin é para vc mover ele na tela
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=15, bottom_right=15),
        shadow=BoxShadow(spread_radius=1, blur_radius=15, color=colors.BLUE, offset=Offset(0, 0),
                         blur_style=ShadowBlurStyle.OUTER),


            content=Column(
                controls=[
                    Row(controls=[
                        Image(src="god.png")
                    ],alignment=MainAxisAlignment.CENTER),
                    Row(
                        controls=[
                            Text("sei la",size=20)
                    ],alignment=MainAxisAlignment.CENTER
                    ),
                    Row(
                        controls=[
                            Text("sei la")
                    ],alignment=MainAxisAlignment.CENTER
                    )
           ],horizontal_alignment="center"
       )

    )
    linha=Row(controls=[contender])
    page.add(linha)
    page.update()
if __name__ == '__main__':
    app(target=main)