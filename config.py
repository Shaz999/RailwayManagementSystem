import mysql.connector

ADMIN_API_KEY = 'waMkHbbdpz-jd7FdS_f7RQ0dI6JtgrSc_p2TQcOg2zM'

JWT_SECRET_KEY = 'rVfQHQlIzm7gG_jcI7vUG6ZUZjcp7fWqaLlRVZLriX8'

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='Sa',
        password='******',
        database='railway_system'
    )
