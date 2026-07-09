from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

if __name__ == '__main__':
    connection_string = 'sqlite:///my_database.db'
    engine = create_engine(connection_string, echo=True)
    conn = engine.connect()
    meta = MetaData()

    people = Table(
        'people',
        meta,
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('age', Integer),
        Column('salary', Integer),
    )

    meta.create_all(engine)

    # insert_statement = people.insert().values(name='Alma', age=22, salary=50000)
    # conn.execute(insert_statement)

    # insert_statement = insert(people).values(name='Pier', age=33, salary=40000)
    # conn.execute(insert_statement)
    # conn.commit()

    # select #1
    select_statement = people.select().where(people.c.age >= 25)
    result = conn.execute(select_statement)

    for row in result.fetchall():
        print(row)

    # update
    update_stmt = people.update().where('Pier' == people.c.name).values(age=66)
    conn.execute(update_stmt)
    conn.commit()

    # select #2 - all
    select_statement = people.select()
    result = conn.execute(select_statement)

    for row in result.fetchall():
        print(row)
