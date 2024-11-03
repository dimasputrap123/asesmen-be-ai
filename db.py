import pymysql
import pymysql.cursors

db_config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'asesmen'
}

# Membuat koneksi
def get_db_connection():
    connection = pymysql.connect(user=db_config['user'],
                                 password=db_config['password'],
                                 host=db_config['host'],
                                 database=db_config['database'])
    return connection

def select(query: str):
    connection = get_db_connection()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def transaction():
    connection = get_db_connection()
    cursor = connection.cursor()
    return cursor

def commit(cursor: pymysql.cursors.Cursor):
    cursor.connection.commit()
    cursor.connection.close()
    cursor.close()

def rollback(cursor: pymysql.cursors.Cursor):
    cursor.connection.rollback()
    cursor.connection.close()
    cursor.close()
