How Start
=========

Virtualenv::

    ~ $ virtualenv env
    ~ $ source env/bin/activate

Clone the app::

    (env) ~ $ git clone https://github.com/AFPy/pyconfr.git
    (env) ~ $ cd pyconfr

Dev install::

    (env) ~/pyconfr $ pip install -r requirements.txt
    (env) ~/pyconfr $ python manage.py syncdb
    (env) ~/pyconfr $ python manage.py loaddata fixtures/*

Start it in dev mode::

    (env) ~/pyconfr $ python manage.py runserver

