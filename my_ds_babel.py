import sqlite3
import pandas
import warnings
warnings.filterwarnings('ignore')

def sql_to_csv(database, table_name):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    query = f"select * from {table_name}"
    results = pandas.read_sql_query(query, conn)
    results.to_csv("list_fault_lines.csv", index=False)
    with open("list_fault_lines.csv",'r') as csvf:
        return csvf.read()[:-1]


def csv_to_sql(csv_content, database, table_name):
    df = pandas.read_csv(csv_content)
    df = df.drop_duplicates()
    conn = sqlite3.connect(database)
    df.to_sql(table_name, con=conn, if_exists='replace', index=False)
