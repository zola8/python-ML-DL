import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

# https://www.youtube.com/watch?v=529LYDgRTgQ - SQLAlchemy Crash Course - Master Databases in Python

def get_connection():
    connection_string = 'sqlite:///:memory:'
    engine = create_engine(connection_string, echo=True)
    return engine, engine.connect()


def insert_test_values():
    rows = [
        ("Rahul", 22, 50000),
        ("Prajwal", 23, 60000),
        ("Ishan", 21, 40000),
    ]

    # Convert to dictionaries
    rows_dict = [
        {"name": name, "age": age, "salary": salary} for name, age, salary in rows
    ]

    session = Session(engine)
    session.execute(text("INSERT INTO people(name, age, salary) VALUES (:name, :age, :salary)"), rows_dict)
    session.commit()


def create_test_table():
    conn.execute(text("CREATE TABLE IF NOT EXISTS people(name VARCHAR(30), age INTEGER, salary INTEGER)"))
    conn.commit()


if __name__ == '__main__':
    print("SQLAlchemy current version:", sqlalchemy.__version__)
    engine, conn = get_connection()

    create_test_table()
    insert_test_values()
