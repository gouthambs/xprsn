# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 16:09:49 2014

@author: Goutham
"""

from app import db, flask_app
from app.auth.views import auth_bp
from app.widgets.views import widg_bp
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

flask_app.config.from_object('config')
flask_app.register_blueprint(auth_bp)
flask_app.register_blueprint(widg_bp)
    
migrate = Migrate(flask_app, db)

manager = Manager(flask_app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

