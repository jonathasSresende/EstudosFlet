from flet import *
# site de icones       https://cupertino-icons.web.app/
def main(page:Page):
    page.title="Estudando Cards"

    produto=Card(
        content=Container(
            bgcolor=colors.YELLOW,
            border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=15, bottom_right=15),
            border=border.only(top=BorderSide(15, color=colors.RED), bottom=BorderSide(15, color=colors.RED),left=BorderSide(5,color=colors.RED),right=BorderSide(5,color=colors.RED)),
            content=Column(
                controls=[
                    Row(controls=[Image(src="hamburger.png")],alignment=MainAxisAlignment.CENTER),
                    Row(controls=[Text("Lanche Vegano",color=colors.RED,weight=FontWeight.W_900)],alignment=MainAxisAlignment.CENTER),
                    Row(controls=[Text("Lache Feito de Proteina Vegetal",color=colors.BLACK,weight=FontWeight.W_900)],alignment=MainAxisAlignment.CENTER),
                    Row(controls=[
                        Icon(cupertino_icons.HEART_CIRCLE,color=colors.RED),
                        Icon(cupertino_icons.MONEY_DOLLAR,color=colors.GREEN)],alignment=MainAxisAlignment.SPACE_EVENLY),
                    Row(controls=[Icon(icons.CHEVRON_RIGHT),Text("35,99",color=colors.RED,weight=FontWeight.W_900,size=30)],alignment=MainAxisAlignment.CENTER)
                ]
            )
        ),width=250,height=250,

    )
    page.add(produto)
if __name__ == '__main__':
    app(main)