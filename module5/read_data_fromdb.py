import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:Welcome%40123@localhost:5432/demo_db", pool_recycle = -1)
db_engine = engine.connect()
print("engine is running")

def query_db(query: str, db_conn: sqlalchemy.engine.base.Connection ):
    df = pd.read_sql(query, db_conn)
    print(df)
    return df

query_db("SELECT * FROM courses LIMIT 5", db_engine)

db_engine.close()

# from sqlalchemy import create_engine
# engine = create_engine('sqlite://', echo=False)
# df.to_sql('users', con=engine)
# engine.execute("SELECT * FROM users").fetchall()
