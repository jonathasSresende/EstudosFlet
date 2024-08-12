from flet import *

def main(page:Page):
    page.title="Mercado Livre"
    page.on_scroll=True # ROLAMENTO DE PAGINA AQUIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
    #listview = ListView(expand=5, spacing=10, padding=25, auto_scroll=True )

    page.bgcolor = colors.YELLOW


# NAO CONSEGUI USAR O FOR
    # variosProdutos=GridView(
    #     expand=1,
    #     runs_count=50,
    #     max_extent=200,
    #     child_aspect_ratio=0.6,
    #     spacing=5,
    #     run_spacing=2
    # )



    contender=Container(
        bgcolor=colors.YELLOW_700,
        margin=margin.all(30),
        border=border.only(top=BorderSide(5, color=colors.WHITE), bottom=BorderSide(5, color=colors.WHITE),
                           left=BorderSide(5, color=colors.WHITE), right=BorderSide(5, color=colors.WHITE)),
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=15, bottom_right=15),
            content=Column(
                width=350,
                height=1000,
                controls=[
                    Row(controls=[
                        Image(src="pngfind.com-livre-png-3678855 (1).png")
                    ],alignment=MainAxisAlignment.CENTER),
                    Row(controls=[
                        Text("""_________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             _________________________\n_________________________\n
                             MERCADO LIVRE
                             """)
                        ],alignment=MainAxisAlignment.CENTER)

                ]
            )
    )
    contender1 = Container(
        bgcolor=colors.BLUE,
        margin=margin.all(30),
        border=border.only(top=BorderSide(5, color=colors.WHITE), bottom=BorderSide(5, color=colors.WHITE),
                           left=BorderSide(5, color=colors.WHITE), right=BorderSide(5, color=colors.WHITE)),
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=15, bottom_right=15),
        content=Column(
            width=250,
            height=200,

            controls=[
                Row(controls=[
                    Image(src="Jbl.png")
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Text("produto")
                ], alignment=MainAxisAlignment.CENTER)

            ]
        )
    )
    contender2 = Container(
        bgcolor=colors.BLUE,
        margin=margin.all(30),
        border=border.only(top=BorderSide(5, color=colors.WHITE), bottom=BorderSide(5, color=colors.WHITE),
                           left=BorderSide(5, color=colors.WHITE), right=BorderSide(5, color=colors.WHITE)),
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=15, bottom_right=15),
        content=Column(
            width=250,
            height=200,

            controls=[
                Row(controls=[
                    Image(src="Jbl.png")
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Text("produto")
                ], alignment=MainAxisAlignment.CENTER)

            ]
        )
    )
    contender3 = Container(
        bgcolor=colors.BLUE,
        margin=margin.all(30),
        border=border.only(top=BorderSide(5, color=colors.WHITE), bottom=BorderSide(5, color=colors.WHITE),
                           left=BorderSide(5, color=colors.WHITE), right=BorderSide(5, color=colors.WHITE)),
        border_radius=border_radius.only(top_left=15, top_right=15, bottom_left=15, bottom_right=15),
        content=Column(
            width=250,
            height=200,

            controls=[
                Row(controls=[
                    Image(src="Jbl.png")
                ], alignment=MainAxisAlignment.CENTER),
                Row(controls=[
                    Text("produto")
                ], alignment=MainAxisAlignment.CENTER)

            ]
        )
    )
    linha=Row(controls=[contender,contender1,contender2,contender3])
    page.add(linha)
    page.update()

if __name__ == '__main__':
    app(main,WEB_BROWSER)