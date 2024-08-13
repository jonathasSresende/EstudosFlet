from flet import app
from  exercicio_de_telas.sistemabancario.main.handle_process import start

if __name__ == '__main__':
    app(target=start,assets_dir="assets")