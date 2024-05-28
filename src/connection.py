import pymysql

def get_connection():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='840862_Mv',
            database='iagroscan'
        )
        return connection
    except pymysql.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None