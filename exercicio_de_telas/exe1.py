# Criar uma aplicação que vai pegar o nome e o endereço da pessoa, pegue a rua, numero, bairro, cep separados
# e vai mostrar na tela em dois elementos Text:
#
# Nome: Carlos
#
# Endereço: Rua srrsrrs Numero srsr CEP:00000

from flet import Page, TextField, Text, app, ElevatedButton

def main (pagina:Page):
    pagina.title="Bordel Amore Desejado"

    pagina.window_max_width=500
    pagina.window_max_height=600

    pagina.window_height=600
    pagina.window_width=500

    pagina.window.center()

    pagina.bgcolor="#FF69B4"

    t_field_nome=TextField(label="Digite seu nome")
    t_field_rua=TextField(label="Rua")
    t_field_num=TextField(label="Nº")
    t_field_bairro=TextField(label="Bairro")

    btn_calcular=ElevatedButton(text="Verificar")

    def verificar (e):
        txt_resposta.value=f"Nome {t_field_nome.value}"
        txt_end.value=f"Rua {t_field_rua.value}, num {t_field_num.value} Bairro {t_field_bairro.value}"
        t_field_nome.value=""
        t_field_rua.value=""
        t_field_num.value=""
        t_field_bairro.value=""

        t_field_nome.update()
        t_field_rua.update()
        t_field_num.update()
        t_field_bairro.update()
        txt_resposta.update()
        txt_end.update()

    btn_calcular.on_click= verificar #aqui é coloco a variavel do def q criei


    txt_resposta=Text(value="", size=20)
    txt_end=Text(value="", size=20)
    pagina.add(t_field_nome)
    pagina.add(t_field_rua)
    pagina.add(t_field_num)
    pagina.add(t_field_bairro)
    pagina.add(btn_calcular)
    pagina.add(txt_resposta)
    pagina.add(txt_end)

    pagina.update()

app(target=main)