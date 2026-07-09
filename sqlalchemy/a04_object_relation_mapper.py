from sqlalchemy import create_engine, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    pass


class People(Base):
    __tablename__ = 'people'

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    age = mapped_column(Integer)
    salary = mapped_column(Integer)

    things = relationship('Thing', back_populates='people')


class Thing(Base):
    __tablename__ = 'things'

    id = mapped_column(Integer, primary_key=True)
    description = mapped_column(String, nullable=False)
    value = mapped_column(Float, default=0.0)
    owner_id = mapped_column(Integer, ForeignKey('people.id'))

    people = relationship('People', back_populates='things')


connection_string = 'sqlite:///my_database.db'
engine = create_engine(connection_string, echo=True)

Base.metadata.create_all(engine)

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()

    new_person = People(name='Charlie', age=80, salary=1500)
    session.add(new_person)
    session.flush()

    new_thing = Thing(description='Charlie''s new thing', value=10.0, owner_id=new_person.id)
    session.add(new_thing)
    session.commit()

    print([t.description for t in new_person.things])
    print(new_thing.people.name)
