from sqlalchemy import Table, Column, Integer, String, MetaData, create_engine, Float, ForeignKey, func


def create_test_tables(engine):
    meta = MetaData()

    people = Table(
        'people',
        meta,
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('age', Integer),
        Column('salary', Integer),
    )

    things = Table(
        'things',
        meta,
        Column('id', Integer, primary_key=True),
        Column('description', String, nullable=False),
        Column('value', Float, default=0.0),
        Column('owner_id', Integer, ForeignKey('people.id')),
    )

    meta.create_all(engine)
    return people, things


if __name__ == '__main__':
    connection_string = 'sqlite:///my_database.db'
    engine = create_engine(connection_string, echo=True)
    conn = engine.connect()

    people, things = create_test_tables(engine)

    insert_people = people.insert().values([
        {'name': 'John', 'age': 22, 'salary': 200},
        {'name': 'Mike', 'age': 23, 'salary': 300},
        {'name': 'Clara', 'age': 24, 'salary': 400},
        {'name': 'Zash', 'age': 33, 'salary': 500},
    ])

    insert_things = things.insert().values([
        {'description': 'laptop', 'value': 300.24, 'owner_id': 1},
        {'description': 'keyboard', 'value': 20, 'owner_id': 1},
        {'description': 'camera', 'value': 500.99, 'owner_id': 2},
        {'description': 'mobile phone', 'value': 400.50, 'owner_id': 2},
        {'description': 'book', 'value': 7.10, 'owner_id': 3},
    ])

    conn.execute(insert_people)
    conn.commit()

    conn.execute(insert_things)
    conn.commit()

    # join_statement = people.join(things, people.c.id == things.c.owner_id)
    join_statement = people.outerjoin(things, people.c.id == things.c.owner_id)

    select_statement = people.select().with_only_columns(
        people.c.name, things.c.description, things.c.value).select_from(join_statement)

    result = conn.execute(select_statement)

    for row in result.fetchall():
        print(row)

    print('-' * 20)
    group_by_statement = things.select().with_only_columns(things.c.owner_id, func.sum(things.c.value)).group_by(
        things.c.owner_id)
    result = conn.execute(group_by_statement)

    for row in result.fetchall():
        print(row)

    print('-' * 20)
    group_by_statement = things.select().with_only_columns(things.c.owner_id, func.sum(things.c.value)).group_by(
        things.c.owner_id).having(func.count(things.c.owner_id) >= 2)
    result = conn.execute(group_by_statement)

    for row in result.fetchall():
        print(row)
