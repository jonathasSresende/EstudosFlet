from flet import *
import math
def main(page:Page):
    page.title="Trabalhando com Container"
    container1=Container(
        content=Text("Texto 1",
                     size=23,
                     weight=FontWeight.W_600,
                     color="#000000"),
        bgcolor=colors.BLUE,
        width=200,
        height=200,
        # padding=45
        # padding=padding.symmetric(vertical=80,horizontal=50),
        # padding= padding.only(top=87, left=50),
        # border=border.all(5,color=colors.RED),
        border=border.only(top=BorderSide(5,color=colors.AMBER_500),bottom=BorderSide(15,color=colors.AMBER_500)),
        margin=margin.all(20),
        # margin= margin.only(top=200,left=150)
        # margin=margin.symmetric(vertical=600)
        # gradient=LinearGradient(
        #     begin=alignment.top_center,
        #     end=alignment.bottom_center,
        #     colors=[colors.BLUE,colors.BLUE_ACCENT_700]
        # )
        # gradient=RadialGradient(
        #     colors=[colors.WHITE, colors.BLUE],
        # )
        # gradient=SweepGradient(
        #     center=alignment.center,
        #     start_angle=0.0,
        #     end_angle=math.pi * 2,
        #     colors=[colors.YELLOW, colors.BLUE],
        # )
        # border_radius=border_radius.all(10)
        border_radius=border_radius.only(top_left=15,top_right=15,bottom_left=10),
        image_src="imgLogin.png",
        shadow=BoxShadow(
        spread_radius=10,# bordinha branca antes da sombra
        blur_radius=25, # desfoque
        color=colors.BLUE_GREY_300,
        offset=Offset(0, 0), # trabalha nos X e Y
        blur_style=ShadowBlurStyle.OUTER, # o tipo de shadow
    ),
        alignment=Alignment(0,0) # ( x, y) o centro do valor é sempre o 0
    )

    container2=Container(
        content=Column(controls=[
            Text("1",bgcolor=colors.RED),
            Text("2",bgcolor=colors.RED),
            Text("3",bgcolor=colors.RED),
            Text("4", bgcolor=colors.RED),
            Text("5", bgcolor=colors.RED),
        ])
        ,
        bgcolor=colors.PINK,
        width=200,
        height=200,
        # padding=45
        # padding=padding.symmetric(vertical=80,horizontal=50),
        # padding= padding.only(top=87, left=50),
        # border=border.all(5,color=colors.RED),
        border=border.only(top=BorderSide(5, color=colors.AMBER_500), bottom=BorderSide(15, color=colors.AMBER_500)),
        margin=margin.all(20),
        # margin= margin.only(top=200,left=150)
        # margin=margin.symmetric(vertical=600)
        # gradient=LinearGradient(
        #     begin=alignment.top_center,
        #     end=alignment.bottom_center,
        #     colors=[colors.BLUE,colors.BLUE_ACCENT_700]
        # )
        # gradient=RadialGradient(
        #     colors=[colors.WHITE, colors.BLUE],
        # )
        # gradient=SweepGradient(
        #     center=alignment.center,
        #     start_angle=0.0,
        #     end_angle=math.pi * 2,
        #     colors=[colors.YELLOW, colors.BLUE],
        # )
        # border_radius=border_radius.all(10)
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=10),
        shadow=BoxShadow(
            spread_radius=10,  # bordinha branca antes da sombra
            blur_radius=25,  # desfoque
            color=colors.BLUE_GREY_300,
            offset=Offset(0, 0),  # trabalha nos X e Y
            blur_style=ShadowBlurStyle.OUTER,  # o tipo de shadow
        ),
        alignment=Alignment(0, 0)  # ( x, y) o centro do valor é sempre o 0
    )
    modal=Container(
        content=Column(
            controls=[
                Row(controls=[
                    Image(src="god.png")
                ], alignment=MainAxisAlignment.CENTER),
                Row(
                    controls=[
                        Text("Titulo1", size=20)
                    ],alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Text("srrrsrsrrsrsrsrsrrssr"
                             "ssrsrrsrsrsrrssrrsrsrsrsrrs"
                             ""
                             "srsrsrrsrsrrs", width=200, text_align=TextAlign.JUSTIFY)
                    ]
                )
            ], horizontal_alignment="center"
        )
    )
    linha=Row(controls=[container1,container1,container2, modal])
    page.add(linha)
    page.update()

if __name__ == '__main__':
    app(target=main)