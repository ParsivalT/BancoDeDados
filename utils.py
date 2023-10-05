from rich.console import Console
from rich.panel import Panel
from time import sleep

CONS = Console()

# Animação para melhorar a experiencia do usuario.
def aniLoad(time:int=1, value:str="Carregando"):
    with CONS.status(f"[bold green][b]{value}[/b]...") as status:
        for _ in range(time):
            sleep(1)

# TODO: Criar o menu com as opções para ADICIONAR, DELETAR, ATUALIZAR

class Sistema():
    def __init__(self):
        pass


    def menu(self):
        CONS.clear()
        titulo = '[b]CRUD - Python[/b]'
        opcao = Panel(
            """
            Selecione uma opção:

            [b]1[/b] - [cyan b]Listar[/] produtos;
            [b]2[/b] - [green b]Inserir[/] produtos;
            [b]3[/b] - [yellow b]Atualizar[/] produtos;
            [b]4[/b] - [red b]Deletar[/] produtos;
            [b]5[/b] - [deep_pink4]Sair[/] do programa.

            [grey]Pressione [b]m[/b] para abrir o menu novamente[/]
        """,title='[b]Gerenciamento de Funcionarios[/b]')

        CONS.rule(title=titulo, align='center')
        CONS.print(opcao)

        input()


