from config import get_db_connection

def get_user_by_username(username):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    return cursor.fetchone()

def create_user(username, password_hash, role):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)", 
                   (username, password_hash, role))
    db.commit()
