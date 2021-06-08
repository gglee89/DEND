import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

def load_staging_tables(cur, conn):
    """
    Execute all queries found in the 'copy_tables_queries' array
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Execute all queries found in the 'insert_tables_queries' array
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """    
    - INITIALIZE the DB instance connection for manipulation
    - EXECUTE load_staging_tables
    - EXECUTE insert_tables
    - TERMINATE the DB instance connection after usage
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()