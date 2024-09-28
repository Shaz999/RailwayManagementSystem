import mysql.connector

ADMIN_API_KEY = 'your_admin_api_key'
JWT_SECRET_KEY = 'your_jwt_secret_key'

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='your_db_user',
        password='your_db_password',
        database='your_database_name'
    )
