# -*- coding: utf-8 -*-
"""
Created on Sun Mar 16 15:34:25 2014

@author: Goutham
"""

#!xprsn-env/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from config import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print 'Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, 
                                                        SQLALCHEMY_MIGRATE_REPO))