from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'asdasdasd'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # views'da ve auth'da oluşturduğumuz blueprintleri 
    # burada da tanımlamamız gerekiyor
    from .views import views


    # url prefix kısmını eğer burda doldurursak 
    # ve daha sonra da modülün kendisinde de doldurursak 
    # localhost bize karmaşık bir link verir
    # bunu ortadan kaldırmak için buradaki 
    # url_prefix değerini boş bırakabiliriz
    app.register_blueprint(views, url_prefix='/')

    return app

