from flet import *
# site de icones       https://cupertino-icons.web.app/
def main(page:Page):
    page.title="Estudando Cards"

    produto=Card(
        content=Container(
            content=Column(
                controls=[
                    Image(src="hamburger.png"),
                    Text("Lanche Vegano"),
                    Text("Lache Feito de Proteina Vegetal"),
                    Row(controls=[
                        Icon(cupertino_icons.HEART_CIRCLE),
                        Icon(icons.PAYMENT)

                    ])


                ]
            )
        )
    )
    page.add(produto)
if __name__ == '__main__':
    app(main)