import os
import sys
from flask import render_template
from app import db
from app import flask_app
from app.auth.models import User

import config

sys.path.append(os.path.join(config.basedir,"app"))


@flask_app.route('/')
def index():
    #u = User('Bbb','B','dddf@d.com')
    #db.session.add(u)
    #db.session.commit()
    #print db
    return render_template('index.html')


def app_setup(app):
    flask_app.config.from_object('config')
    flask_app.secret_key  = config.SECRET_KEY
    # all models have to be loaded at this point
    
    #with flask_app.app_context():
    #    from app.widgets.models import Widget        
    #    from app.auth.models import User    
    #    
    #    db.create_all()

if __name__ == '__main__':

    app_setup(flask_app)
    
    flask_app.run(debug=True)