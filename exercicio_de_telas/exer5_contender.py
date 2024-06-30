from flet import *

def main (page:Page):
    page.title="Cardapio Das Mina"

    contender=Container(
        bgcolor=colors.PINK_50,
        width=200,
        height=300,
        margin=margin.all(40),
        border=border.only(top=BorderSide(5, color=colors.PINK), bottom=BorderSide(5, color=colors.PINK),left=BorderSide(5,color=colors.PINK),right=BorderSide(5,color=colors.PINK)),
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=15, bottom_right=15),
        shadow=BoxShadow(spread_radius=1, blur_radius=15, color=colors.PINK, offset=Offset(0, 0),blur_style=ShadowBlurStyle.OUTER),
        padding=padding.only(top=15),

            content=Column(
                controls=[
                    Row(controls=[
                        Image(src="Brand love2.png"),Icon(cupertino_icons.CHECKMARK_SEAL_FILL,color=colors.GREEN)
                    ],alignment=MainAxisAlignment.CENTER),
                    Row(
                        controls=[
                            Text("♦☻♥ Laticha ♦☻♥",size=15,color=colors.PINK_700,weight=FontWeight.W_900)
                    ],alignment=MainAxisAlignment.CENTER
                    ),
                    Row(
                        controls=[
                            Text("Sou uma gatinha fogosa \nque gosta de carinho mas \ntambém gosta, de love \nmais selvagem.",size=10,color=colors.PINK_700,weight=FontWeight.W_300)
                    ],alignment=MainAxisAlignment.CENTER
                    ),
                    Row(
                        controls=[
                            Icon(cupertino_icons.MONEY_DOLLAR,color=colors.GREEN),Text("150,00",size=15,weight=FontWeight.W_900,color=colors.PINK_500),
                            Icon(cupertino_icons.MAIL,color=colors.PINK_700)
                        ], alignment=MainAxisAlignment.CENTER
                    ),
                    Row(
                        controls=[
                            Icon(cupertino_icons.PHONE,color=colors.BLUE),Text("11 97573-4461",size=15,color=colors.RED,weight=FontWeight.W_800)
                        ],alignment=MainAxisAlignment.CENTER
                    )
           ],horizontal_alignment="center"
       )

    )

    contender1 = Container(
        bgcolor=colors.BLUE_100,
        width=200,
        height=300,
        border=border.only(top=BorderSide(5, color=colors.CYAN_500), bottom=BorderSide(5, color=colors.CYAN_500),
                           left=BorderSide(5, color=colors.CYAN_500), right=BorderSide(5, color=colors.CYAN_500)),
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=15, bottom_right=15),
        shadow=BoxShadow(spread_radius=1, blur_radius=15, color=colors.BLUE, offset=Offset(0, 0),
                         blur_style=ShadowBlurStyle.OUTER),
        padding=padding.only(top=15),

        content=Column(
            controls=[
                Row(controls=[
                    Image(src="mia3.png",width=100,height=100),Icon(cupertino_icons.CHECKMARK_SEAL)
                ], alignment=MainAxisAlignment.CENTER),
                Row(
                    controls=[
                        Text("♦☻♥ Esteffany ♦☻♥", size=15, color=colors.PINK_700, weight=FontWeight.W_900)
                    ], alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Text(
                            "Sou uma morena ardente \nque gosta de um anal e \ngosto, de tapa na cara,\n           Me Liga.",
                            size=10, color=colors.PINK_700, weight=FontWeight.W_300)
                    ], alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Icon(cupertino_icons.MONEY_DOLLAR, color=colors.GREEN),
                        Text("150,00", size=15, weight=FontWeight.W_900, color=colors.PINK_500),
                        Icon(cupertino_icons.MAIL, color=colors.PINK_700)
                    ], alignment=MainAxisAlignment.CENTER
                ),
                    Row(
                        controls=[
                            Icon(cupertino_icons.PHONE,color=colors.BLUE),Text("11 97883-4001",size=15,color=colors.RED,weight=FontWeight.W_800)
                        ],alignment=MainAxisAlignment.CENTER
                    )
            ], horizontal_alignment="center"
        )

    )

    contender2 = Container(
        bgcolor=colors.PURPLE_100,
        width=200,
        height=300,
        margin=margin.all(40),
        border=border.only(top=BorderSide(5, color=colors.PURPLE), bottom=BorderSide(5, color=colors.PURPLE),
                           left=BorderSide(5, color=colors.PURPLE), right=BorderSide(5, color=colors.PURPLE)),
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=15, bottom_right=15),
        shadow=BoxShadow(spread_radius=1, blur_radius=15, color=colors.PURPLE, offset=Offset(0, 0),
                         blur_style=ShadowBlurStyle.OUTER),
        padding=padding.only(top=15),

        content=Column(
            controls=[
                Row(controls=[
                    Image(src="Pabllo_Vittar.png"),Icon(cupertino_icons.CHECKMARK_SEAL)
                ], alignment=MainAxisAlignment.CENTER),
                Row(
                    controls=[
                        Text("♦☻♥ Tifanny ♦☻♥", size=15, color=colors.PINK_700, weight=FontWeight.W_900)
                    ], alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Text(
                            "Sou uma morena Trans que\ngosta de um 69 gostoso e \ngosto de uma pegada forte\n           Me Liga.",
                            size=10, color=colors.PINK_700, weight=FontWeight.W_300)
                    ], alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Icon(cupertino_icons.MONEY_DOLLAR, color=colors.GREEN),
                        Text("150,00", size=15, weight=FontWeight.W_900, color=colors.PINK_500),
                        Icon(cupertino_icons.MAIL, color=colors.PINK_700)
                    ], alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Icon(cupertino_icons.PHONE, color=colors.BLUE),
                        Text("11 97573-4789", size=15, color=colors.RED, weight=FontWeight.W_800)
                    ], alignment=MainAxisAlignment.CENTER
                )
            ], horizontal_alignment="center"
        )

    )
    linha=Row(controls=[contender,contender1,contender2])
    page.add(linha)
    page.update()
if __name__ == '__main__':
    app(target=main)



    100
    109
    96