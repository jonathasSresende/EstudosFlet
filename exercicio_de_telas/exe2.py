#Criar uma aplicação que a pessoa vai digitar o salário e vc vai
#calcular quanto é 10% desse salario e mostrar a resposta na tela


from flet import Page, TextField, Text, app, ElevatedButton

def main (pagina:Page):
    pagina.title= "Salario da puta"
    pagina.window_max_width=600
    pagina.window_max_height=600

    pagina.window_height=600
    pagina.window_width=600

    pagina.window.center()

    pagina.bgcolor="#87CEFA"

    t_field_salario=TextField(label="Valor do salario")

    btn_calcular=ElevatedButton(text="Calcular")

    def calcular (e):
        valorSalario=float(t_field_salario.value)
        valorDaPorcentagem=valorSalario * 0.10
        txt_resposta.value=f"seu salario é R$ {valorSalario:.2f} \n e 10% do seu salario é R$ {valorDaPorcentagem:.2f}"# :.2f => vc deixa duas casa decimal

        t_field_salario.update()
        txt_resposta.update()

    btn_calcular.on_click=calcular



    txt_resposta=Text(value="Resposta",size=40)


    pagina.add(t_field_salario)
    pagina.add(btn_calcular)
    pagina.add(txt_resposta)

    pagina.update()

app(target=main)



