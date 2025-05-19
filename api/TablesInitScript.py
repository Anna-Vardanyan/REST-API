from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey, Date, Float, JSON
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("NEW_OWNER_NAME")
DB_PASSWORD = os.getenv("NEW_OWNER_PASSWORD")
DB_HOST = "192.168.5.55"
DB_PORT = 7777
DB_NAME = "apiproject"

Base = declarative_base()

class Operator(Base):
    __tablename__ = 'operator'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    operator_code = Column(String, nullable=False)
    number_count = Column(Integer, nullable=False)

    connections = relationship("Connection", back_populates="operator")


class Subscriber(Base):
    __tablename__ = 'subscriber'
    id = Column(Integer, primary_key=True, autoincrement=True)
    passport_data = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    address = Column(String, nullable=False)

    connections = relationship("Connection", back_populates="subscriber")


class Connection(Base):
    __tablename__ = 'connection'
    id = Column(Integer, primary_key=True, autoincrement=True)
    operator_id = Column(Integer, ForeignKey('operator.id'), nullable=False)
    subscriber_id = Column(Integer, ForeignKey('subscriber.id'), nullable=False)
    phone_number = Column(String, nullable=False)
    tariff_plan = Column(String, nullable=False)
    debt = Column(Float, nullable=False)
    installation_date = Column(Date, nullable=False)
    meta_data = Column(JSON, nullable=True)

    operator = relationship("Operator", back_populates="connections")
    subscriber = relationship("Subscriber", back_populates="connections")


def init_db():
    DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    try:
        engine = create_engine(DATABASE_URL, echo=True)
        Base.metadata.create_all(engine)
        print("Tables created successfully!")

        Session = sessionmaker(bind=engine)
        session = Session()
        print("Database session initialized.")
        return session
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    session = init_db()