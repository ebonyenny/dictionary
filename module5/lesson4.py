import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:Welcome%40123@localhost:5432/demo_db", pool_recycle = -1)
#creating a connection; i used raw connection because i got a cursor attribute error.
my_engine = engine.raw_connection()
# df = engine.connect()
#commented out the way i connected using connect()
print("engine is running") #to confirm connection

#insert my csv file into a dataframe
df= pd.read_csv('C:\\Users\\Dorcas\\Desktop\\SGI 1.3\\python basics\\module5\\users.csv', index_col=0)
df.head()
# df.to_sql(users if_exists='replace', index=True, index_label=None, method=None)

#read data to the database and assign to variable sql
# sql = """COPY users(name, account, is_group, salary)
# FROM 'C:\\Users\\Dorcas\\Desktop\\SGI 1.3\\users.csv'
# DELIMITER ','
# CSV HEADER;"""



df.to_sql('users_new', con=engine)

# engine.execute("SELECT * FROM users").fetchall()