import os
import sys
from flask import render_template

from app import db,flask_app
from app.auth.views import auth_bp
from app.widgets.views import widg_bp

import config

sys.path.append(os.path.join(config.basedir,"app"))


@flask_app.route('/')
def index():
    return render_template('index.html')


def app_setup(app):
    flask_app.config.from_object('config')
    flask_app.secret_key  = config.SECRET_KEY
    # all models have to be loaded at this point
    flask_app.register_blueprint(auth_bp)
    flask_app.register_blueprint(widg_bp)
    #with flask_app.app_context():
    #    from app.widgets.models import Widget        
    #    from app.auth.models import User    
    #    
    #    db.create_all()

if __name__ == '__main__':

    app_setup(flask_app)
    
    flask_app.run(debug=True)