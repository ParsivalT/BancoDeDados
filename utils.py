from rich.console import Console
from time import sleep

console = Console()

# Animação para melhorar a experiencia do usuario.
def aniLoad(time:int=1, value:str="Carregando"):
    with console.status(f"[bold green]{value}...") as status:
        for _ in range(time):
            sleep(1)

# TODO: Criar o menu com as opções para ADICIONAR, DELETAR, ATUALIZAR
def menu():
    pass
