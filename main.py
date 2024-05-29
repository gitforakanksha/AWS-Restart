from sqlmodel import Field, SQLModel, create_engine, Session
# from sqlalchemy import text
# from sqlalchemy import UniqueConstraint -> if you want unique constraint on name values


class Hero(SQLModel, table=True):
    # __table_args__ = (UniqueConstraint("name"),) -> if you want unique constraint on name values
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


sqlite_file_name = "database.db"

sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_heroes():
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spiderman", secret_name="Peter Parker")

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)

        session.commit() # INSERT, UPDATE, DELETE

    # with Session(engine) as session:
    #     result = session.execute(text("SELECT * FROM hero"))
    #     heroes = [row for row in result]
    #     print(heroes)


if __name__ == "__main__":
    create_db_and_tables()
    create_heroes()
