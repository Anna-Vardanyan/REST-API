from pydantic import BaseModel
from datetime import date
from typing import Any

class OperatorBase(BaseModel):
    name: str
    operator_code: str
    number_count: int

class OperatorCreate(OperatorBase):
    pass

class Operator(OperatorBase):
    id: int

    class Config:
        orm_mode = True

class SubscriberBase(BaseModel):
    passport_data: str
    full_name: str
    address: str

class SubscriberCreate(SubscriberBase):
    pass

class Subscriber(SubscriberBase):
    id: int

    class Config:
        orm_mode = True

class ConnectionBase(BaseModel):
    operator_id: int
    subscriber_id: int
    phone_number: str
    tariff_plan: str
    debt: float
    installation_date: date
    meta_data: Any

class ConnectionCreate(ConnectionBase):
    pass

class Connection(ConnectionBase):
    id: int

    class Config:
        orm_mode = True
