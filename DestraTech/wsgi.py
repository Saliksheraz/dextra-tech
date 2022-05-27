"""
WSGI config for respberyyPi project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'respberyyPi.settings')

application = get_wsgi_application()

# from pymongo import MongoClient
# client = MongoClient('mongodb+srv://Salik:JFAVPkCgW8mtXRN@cluster0.p1m4g.mongodb.net/NodesData?retryWrites=true&w=majority')
# allDatabases = client.list_databases()
# database = client['warehouse386']
# collection = database['compartmentsinfos']
# cursor = collection.find({})
# for document in cursor:
#     print(document['boxstate'])
