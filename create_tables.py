import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """Drops the tables of the database
    @cur: database cursor
    @conn: database connection"""
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """Runs the creating tables queries
    @cur: database cursor
    @conn: database connection"""
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """Executes above written functions and gets the
    datawarehouse config document"""
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()