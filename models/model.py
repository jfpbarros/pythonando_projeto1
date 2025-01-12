from sqlmodel import Field, SQLModel, create_engine, Relationship
from typing import Optional
from datetime import date
from decimal import Decimal


class Subscription(SQLModel, table=True): #transforma uma classe em uma tabela
    id: int = Field(primary_key=True)
    empresa: str
    site: Optional[str] = None
    data_assinatura: date
    valor: Decimal #É recomendado que não use float para valores monetários no Python.
    status: int

class Payments(SQLModel, table=True):
    id: int = Field(primary_key=True)
    subscription_id: int = Field(foreign_key="subscription.id")
    subscription: Subscription = Relationship()
    date: date


