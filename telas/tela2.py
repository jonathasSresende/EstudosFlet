from flet import Page, TextField, ElevatedButton,app,Text

# Page : é usado para criar e configurar a aparencia da pagina, na verdade do projeto
# é nela q trabalhamos as routes (rotas) de novas telas;
#
# TextField: Campo de entrada de texto, no qual entramos com dados podemos configurar
#
# ElevatedButton: que nada mais é q um botao

def main(pagina:Page):
    #esse parametro vai ter tudo q uma Page faz e tem
    pagina.title="Segunda Tela" #titulo da pagina

    #window_max quer dizer q vc só pode abrir ate essa medida
    pagina.window_max_width=600 #tamanho da tela q eu quero altura
    pagina.window_max_height=700 #tamanho da tela q eu quero Largura

    #essa é a largura real dela
    pagina.window_width=600
    pagina.window_height=700

    #tamanho minimo
    pagina.window_min_width=400
    pagina.window_min_height=550

    #para deixa no centro
    pagina.window_center()

    #cor entra na pagina https://celke.com.br/artigo/tabela-de-cores-html-nome-hexadecimal-rgb
    pagina.bgcolor="#808080"


    #Colocando elementos na tela
    t_field_nome=TextField(label="Digite seu nome")   #o TextField me permite
    t_field_salario=TextField(label="salario",prefix_text="R$")

    #o texto q aparece dentro do botao
    btn_calcular=ElevatedButton(text="Calcular")

    def calculando(e):
        #eu posso pegar o valor de dentro do textfild usando o atributo value
        txt_resposta.value=f"Nome: {t_field_nome.value}, tem o salario R${t_field_salario.value}"
        t_field_nome.value=""
        t_field_nome.update()
        t_field_salario.value=""
        t_field_salario.update()
        txt_resposta.update()


    # toda vez q fazer um evento é construido dentro de uma funçao
    btn_calcular.on_click = calculando


    # O value vai ser o valor inicial do nosso texto
    # o size vai modifica o tamanho do texto
    txt_resposta=Text(value="Resposta", size=50)


    #estou usando o add para adcinar elementos na minha tela
    pagina.add(t_field_nome)
    pagina.add(t_field_salario)
    pagina.add(btn_calcular)
    pagina.add(txt_resposta)

    pagina.update()


# ela carrega a nossa pagina ou no nosso projeto
# ela e responsavel de determinar se vai ser uma aplicacao local ou web
app(target=main)
