from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'berkay'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # views'da ve auth'da oluşturduğumuz blueprintleri 
    # burada da tanımlamamız gerekiyor
    from .views import views
    from .auth import auth

    # url prefix kısmını eğer burda doldurursak 
    # ve daha sonra da modülün kendisinde de doldurursak 
    # localhost bize karmaşık bir link verir
    # bunu ortadan kaldırmak için buradaki 
    # url_prefix değerini boş bırakabiliriz
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('database created!')