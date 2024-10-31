import pymysql
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def connect_to_database():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def get_tank_news(connection):
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM ustank_cn"
            cursor.execute(sql)
            result = cursor.fetchall()
        return result
    except pymysql.MySQLError as e:
        print(f"Error fetching data: {e}")
        return []
