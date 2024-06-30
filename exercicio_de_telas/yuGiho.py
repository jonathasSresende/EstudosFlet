from flet import *

def main (page:Page):
    page.title="Cards de Yu-GI-HO"
    page.bgcolor = "#4B0082"
    contender=Container(
        width=350,
        height=550,
        bgcolor="#8A2BE2",
        border=border.only(top=BorderSide(10,color="#9400D3"),bottom=BorderSide(10,color="#9400D3"),
                           right=BorderSide(10,color="#9400D3"),left=BorderSide(10,color="#9400D3")),
        shadow=BoxShadow(spread_radius=1, blur_radius=15, color=colors.PURPLE, offset=Offset(0, 0),
                         blur_style=ShadowBlurStyle.OUTER),

        content=Column(
            controls=[
                Row(controls=[
                    Text("Mago Negro",size=30,weight=FontWeight.W_900,italic=True)
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Image(src="magoNegro.png")
                ],alignment=MainAxisAlignment.CENTER),

                Row(controls=[
                    Text("Seu ataque é o Spellbinding Circle capaz \nde imobilizar seu inimigo. Mago da Ilusão",size=13,italic=True)
                ],alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Text("Atk 2500",weight=FontWeight.W_900),Text("Def 2100",weight=FontWeight.W_900)
                ],alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    ElevatedButton("atack",),ElevatedButton("Defender",)
                ],alignment=MainAxisAlignment.START,),

            ]
        )

    )

    contender2 = Container(
        width=350,
        height=550,
        margin=(40),
        bgcolor="#8A2BE2",
        border=border.only(top=BorderSide(10, color="#9400D3"), bottom=BorderSide(10, color="#9400D3"),
                           right=BorderSide(10, color="#9400D3"), left=BorderSide(10, color="#9400D3")),
        shadow=BoxShadow(spread_radius=1, blur_radius=15, color=colors.PURPLE, offset=Offset(0, 0),
                         blur_style=ShadowBlurStyle.OUTER),

        content=Column(
            controls=[
                Row(controls=[
                    Text("EXODIA", size=30, weight=FontWeight.W_900, italic=True)
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Image(src="Exodia.png")
                ], alignment=MainAxisAlignment.CENTER),

                Row(controls=[
                    Text("Obliterar: Um feixe de energia de poder\ninfinito, que aniquila seu alvo\nimediatamente. Fraquezas: Nenhuma.",
                         size=13, italic=True)
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Text("Atk Infinito", weight=FontWeight.W_900), Text("Def Infinito", weight=FontWeight.W_900)
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    ElevatedButton("atack"), ElevatedButton("Defender")
                ], alignment=MainAxisAlignment.START ),

            ]
        )

    )

    contender3 = Container(
        width=350,
        height=550,
        bgcolor="#8A2BE2",
        border=border.only(top=BorderSide(10, color="#9400D3"), bottom=BorderSide(10, color="#9400D3"),
                           right=BorderSide(10, color="#9400D3"), left=BorderSide(10, color="#9400D3")),
        shadow=BoxShadow(spread_radius=1, blur_radius=15, color=colors.PURPLE, offset=Offset(0, 0),
                         blur_style=ShadowBlurStyle.OUTER),

        content=Column(
            controls=[
                Row(controls=[
                    Text("Dragão Branco dos Olhos Azuis", size=20, weight=FontWeight.W_900, italic=True)
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Image(src="Dragao de Olhos Azul.png")
                ], alignment=MainAxisAlignment.CENTER),

                Row(controls=[
                    Text("White Dragon é capaz de voar com suas asas.\nEmbora não se sabe se ela é capaz de cuspir fogo\ncomo um dragão convencional,\nela é capaz de disparar uma poderosa\nonda de luz da sua boca.",
                         size=13, italic=True)
                ],alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Text("Atk 3000", weight=FontWeight.W_900), Text("Def 2500", weight=FontWeight.W_900)
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    ElevatedButton("atack"), ElevatedButton("Defender")
                ], alignment=MainAxisAlignment.START, ),

            ]
        )

    )
    linha=Row(controls=[contender,contender2,contender3])
    page.add(linha)
    page.update()
if __name__ == '__main__':
    app(main)


