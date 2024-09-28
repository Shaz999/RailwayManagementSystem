from flask import Flask
from flask_jwt_extended import JWTManager
from routes.admin_routes import admin_bp
from routes.user_routes import user_bp
from config import JWT_SECRET_KEY

app = Flask(__name__)
app.config['rVfQHQlIzm7gG_jcI7vUG6ZUZjcp7fWqaLlRVZLriX8'] = JWT_SECRET_KEY
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(admin_bp)
app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(debug=True)
