How Start
=========

Installation
------------

May be you have a specific pyconfr user::

    ~$ cd /home/pyconfr
    ~/home/pyconfr$ sudo -u pyconfr bash

Clone the app::

    ~/home/pyconfr$ git clone https://github.com/AFPy/pyconfr.git
    ~/home/pyconfr$ cd pyconfr

Dev install::

    ~/home/pyconfr/pyconfr$ python bootstrap.py
    ~/home/pyconfr/pyconfr$ ./bin/buildout

Db init::

    ~/home/pyconfr/pyconfr$ ./bin/django syncdb
    ~/home/pyconfr/pyconfr$ ./bin/django loaddata fixtures/*

Start it in dev mode::

    ~/home/pyconfr/pyconfr$ ./bin/django runserver

Start behind apache proxy::

    ~/home/pyconfr/pyconfr$ ./bin/django run_gunicorn localhost:8002 -D

Traductions
-----------

Extraction des messages (en ignorant les applis de bases, et afin d'ajouter les
trads utiles uniquement)::

    ~/home/pyconfr/pyconfr$ ./bin/django makemessages -l fr --ignore=var/*

Edition du po::

    ~/home/pyconfr/pyconfr$ vim conf/locale/fr/LC_MESSAGES/django.po

Compiler les nouveaux messages::

    ~/home/pyconfr/pyconfr$ ./bin/django compilemessages

