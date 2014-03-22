# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 23:12:14 2014

@author: Goutham
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#####################################
# Database Related Configurations   #
#####################################

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')



#####################################
# General Site Configurations       #
#####################################

SITENAME = "XPRSN"
CSRF_ENABLED = True
SECRET_KEY = "secretasdfa;lkj2093poaj092-92i-0ipi--9"
CSRF_SECRET_KEY = "ajsdlfahsqy34982yiH(*^(*)(*&)S(FSOFI))"

