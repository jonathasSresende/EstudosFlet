from exercicio_de_telas.sistemabancario.views.viewCadastro import ViewCadastro
class ControllerCadastrar:
    def __init__(self,telaCadastrar:ViewCadastro)->None:
        self.opcoes=telaCadastrar

        self.btnCadastrar=telaCadastrar.btn_cadastrar
        self.t_field_login=telaCadastrar.t_field_login
        self.t_field_senha=telaCadastrar.t_field_senha
        self.t_field_email=telaCadastrar.t_field_email
        self.t_field_telefone=telaCadastrar.t_field_telefone
        self.t_field_saldo=telaCadastrar.t_field_saldo
        self.btnCadastrar.on_click=self.trocarDePagina


    def trocarDePagina(self,e):
        print("Eu vou troca de tela")
        self.opcoes.page.go("/operacoes")