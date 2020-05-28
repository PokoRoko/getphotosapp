from db.execute_query import execute_query


def create_db():
    with open('../db/create_table_query.sql') as q1:
        create_table_db: str = q1.read()
        execute_query(create_table_db)


if __name__ == "__main__":
    create_db()