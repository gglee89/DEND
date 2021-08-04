import configparser
import sys
import psycopg2
import sql_queries

def connect_db():
    """
        Connects to DB (AWS Redshift)
        
        :return: DB Connection
    """
    config = configparser.ConfigParser()
    config.read_file(open('config/dwh.cfg'))
    con = psycopg2.connect(
      "host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values())
    )
    cur = con.cursor()
    
    con.close()
    
    return cur, con
    

def drop_tables(con, cur):
    """
        Drop tables in DB
        
        :param con: DB Connection
        :param cur: DB Cursor
    """
    try:
      for query in sql_queries.drop_tables:
        cur.execute(query)
        con.commit()
    except TypeError as e:
      print("TypeError {}".format(e))
    except:
      print("Unexpected error:", sys.exc_info()[0])
      raise


def create_tables(con, cur):
    """
        Create tables in DB if it doesns't exist
        
        :param con: DB Connection
        :param cur: DB Cursor
    """
    try:
      for query in sql_queries.create_tables:
        cur.execute(query)
        con.commit()
    except TypeError as e:
      print("TypeError {}".format(e))
    except:
      print("Unexpected error:", sys.exc_info()[0])
      raise
    
    
def main():
    """
        Main executor
        - Connect to DB
        - [Redshift] drop existing tables
        - [Redshift] create tables if it doesn't exist
    """
    cur, con = connect_db()    
    
    drop_tables(con, cur)
    create_tables(con, cur)
    
    con.close()
    
    
if __name__ == "__main__":
    main()