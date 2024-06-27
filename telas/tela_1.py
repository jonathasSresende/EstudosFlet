# flet--version ->  pip install     para instalar
#
#
# no cmd e dentro do phyton entrar na bli

import flet as ft


# isso estou criando meu layout da pagina
def main(page:ft.Page):
    page.title="Primeira Pagina"

    #criando um texto
    tf_nome=ft.TextField(label="digite o seu nome")
    #criando um botao
    btn_cadastrar=ft.ElevatedButton(text="cadastrar")


    #criando um evento
    def enviarNome(e):
        print(tf_nome.value)
    #quando o botao for clicado ele vai copiar o q o tf nome digitou
    btn_cadastrar.on_click=enviarNome

    #aqui estou fazendo q nem o apendi
    page.add(tf_nome)
    page.add(btn_cadastrar)

    # Toda vez q eu alterar a minha pagina eu devo dar um update
    page.update()

if __name__ == '__main__':
    ft.app(main)