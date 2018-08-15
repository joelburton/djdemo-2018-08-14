Sample Django App
=================

This the sample Django app built in the 2018/08/14
"First Steps with Django" presentation.

To play with this:

  $ git clone this-repo
  $ cd djdemo

  $ python -m virtualenv venv
  $ source venv/bin/activate
  $ pip install -r requirements.txt

  $ python manage.py migrate
  $ python manage.py createsuperuser

  $ python manage.py runserver

And then visit http://localhost:8000/admin/
and http://localhost:8000/tasks/

Or: just browse this code for a sense of what we did,
and look at tutorials like:

- the Django tutorial in the docs

- the DjangoGirls tutorial

- Hello Web App, an awesome non-programmer-friendly book on Django


Good luck! joel@joelburton.com


