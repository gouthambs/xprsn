# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 00:11:33 2014

@author: Goutham
"""

#!xprsn-env/bin/python
from migrate.exceptions import DatabaseAlreadyControlledError
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
from webapp import db
import os.path


try:
    db.create_all()
    if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
        api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(SQLALCHEMY_DATABASE_URI, 
                            SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(SQLALCHEMY_DATABASE_URI, 
                            SQLALCHEMY_MIGRATE_REPO, 
                            api.version(SQLALCHEMY_MIGRATE_REPO))
except DatabaseAlreadyControlledError:
    print "Oops! Looks like databse already exists!"