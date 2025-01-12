from sqlmodel import SQLModel, create_engine
from .model import *


sqlite_file_name = 'bdassinaturas.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=True) #Conexão entre o python e o banco de dados.
#echo mostra as informacoes de SQL que está acontecendo.
def create_db_and_table():
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)


if __name__=="__main__":#__main__ 
    create_db_and_table()