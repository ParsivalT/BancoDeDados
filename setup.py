from crud.database import Database
from utils import aniLoad, Sistema

aniLoad(time=2, value="Conectando-se ao banco de dados")
sis = Sistema()
while True: 
    sis.menu()