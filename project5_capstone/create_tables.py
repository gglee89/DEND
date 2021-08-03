import psycopg2
from sql_queries import create_tables, drop_tables

def create_database():
    """
        Connects to DB (AWS Redshift)
        
        :return: DB Connection
    """
    
    
def drop_tables(con, cur):
    """
        Drop tables in DB
        
        :param con: DB Connection
        :param cur: DB Cursor
    """
    

def create_tables(con, cur):
    """
        Create tables in DB if it doesns't exist
        
        :param con: DB Connection
        :param cur: DB Cursor
    """
    
    
def main():
    """
        Main executor
        - Connect to DB
        - [Redshift] drop existing tables
        - [Redshift] create tables if it doesn't exist
    """
    con = connect_db()
    cur = con.cursor()
    
    drop_tables(con, cur)
    create_tables(con, cur)
    
    con.close()
    
    
if __name__ == "__main__"":
    main()