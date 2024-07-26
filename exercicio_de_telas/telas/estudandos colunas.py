# Estudando colunas
# A control that displays its children in a vertical array.
from flet import *
def main(page:Page):
    page.title="Coluna"
    listview=ListView(expand=1, spacing=10, padding=25, auto_scroll=True,)
    gridview=GridView(
        expand=1,
        runs_count=50,
        max_extent=200,
        child_aspect_ratio=0.6,
        spacing=5,
        run_spacing=2
    )
    # coluna=Column(spacing=10)
    # for i in range(10):
    #
    #     coluna.controls.append(
    #         Container(content=Text(f"Texto {i}"), width=200,height=200, bgcolor=colors.INDIGO_100,
    #                   shadow=BoxShadow(spread_radius=10,blur_radius=20,color=colors.INDIGO_400),
    #                   alignment=Alignment(0,0))
    #     )
    for i in range(40):
        gridview.controls.append(
            Container(
                bgcolor=colors.CYAN_50,
                content=Column(
                    controls=[
                        Image(src="hamburger.png"),
                        Row(controls=[Text("Título", size=20, color=colors.BLACK, weight=FontWeight.BOLD)],
                            alignment=MainAxisAlignment.CENTER), # aqui é a linha que trabalha com o título
                        Row(controls=[Column(
                                            controls=[
                                                Text(f"Loja {i}",size=14),
                                                Text("Lanches", size=10, color=colors.GREY_50),
                                                Row(controls=[
                                                    Icon(icons.CIRCLE, color=colors.GREEN_100, size=10),
                                                    Text("Aberto", size=10)
                                                            ], alignment=MainAxisAlignment.START)
                                                    ], alignment=MainAxisAlignment.START
                                            ),# aqui acaba a primeira coluna de conteudo
                                     Column(controls=[
                                                    Text("de R$ 45,90 por:", size=14),
                                                    Text("R$ 27,00", size=20, color=colors.GREEN_100)
                                                    ],horizontal_alignment=CrossAxisAlignment.END
                                          )

                                    ], alignment=MainAxisAlignment.SPACE_BETWEEN
                        ) # Aqui acaba a linha que fala sobre o conteudo da loja

                    ]# Aqui esta o controls da minha coluna
                ) # aqui esta acabando a minha coluna
            )# Aqui esta acabando o meu Container
        )

    page.add(gridview)
    page.update()

if __name__ == '__main__':
    app(main)
