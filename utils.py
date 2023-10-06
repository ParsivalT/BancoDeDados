from crud.database import Database
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from time import sleep

CONS = Console()
PROMPT = Prompt()

# Animação para melhorar a experiencia do usuario.
def aniLoad(time:int=1, value:str="Carregando"):
    with CONS.status(f"[bold green][b]{value}[/b]...") as status:
        for _ in range(time):
            sleep(1)

# TODO: Criar o menu com as opções para ADICIONAR, DELETAR, ATUALIZAR

class Sistema(Database):
    def __init__(self):
        pass


    def menu(self):
        CONS.clear()

        titulo = '[b]CRUD - Python[/b]'
        opcao = Panel(
            """
            Selecione uma opção:

            [b]1[/b] - [cyan b]Buscar[/] Funcionario;
            [b]2[/b] - [green b]Cadastrar[/] Funcionario;
            [b]3[/b] - [yellow b]Atualizar[/] Cadastro;
            [b]4[/b] - [red b]Deletar[/] Funcionario;
            [b]5[/b] - [deep_pink4]Sair[/] do programa.

            [grey]Pressione [b]m[/b] para abrir o menu novamente[/]
        """, title='[b]Gerenciamento de Funcionarios[/b]')

        CONS.rule(title=titulo, align='center')
        CONS.print(opcao)

        self.get_input()


    def conectar(self, dbpath:str) -> None:

        CONS.clear()
        super().__init__(dbpath)
        CONS.print("[bold green][b]Conectado com Sucesso![/b]")
        sleep(1)


    def consultar(self) -> None:
        id: int = 0
        id = int(input(">> "))
        # id = PROMPT.ask(prompt='Insira o [b]id[/b] que deseja consultar')
        resultado = self.mostrar_registro(id=id)

        if resultado is not None:
            CONS.prin(resultado)

        else: 
            CONS.print("[red i] Houve um problema, tente novamente...")

    def get_input(self):
        try: 
            if super().online != False:
                opc = PROMPT.ask("\n>>", default='1').lower()

                match opc:
                    # Buscar
                    case '1': 
                        self.consultar()

                    # Cadastrar
                    case '2':
                        pass

                    # Atualizar
                    case '3':
                        pass

                    # Deletar
                    case '4':
                        pass
                    
                    # Sair
                    case '5' | 'sair' | 'exit':
                        pass
                    case _:
                        raise ValueError

        except ValueError:
            CONS.print('[red i ] Opção invalida')