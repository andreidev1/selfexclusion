from flask import Flask
from flask_migrate import Migrate




def create_app():

    app = Flask(__name__, subdomain_matching=True)

    app.config.from_object('config.Config')

    from db import db
    db.init_app(app)
    
    Migrate(app, db)
    

    with app.app_context():
        from book_app.site.routes import site
        from book_app.api.routes import api_v1
        from book_app.admin.routes import admin
        
        app.register_blueprint(site)
        app.register_blueprint(api_v1)
        app.register_blueprint(admin)

    return app

