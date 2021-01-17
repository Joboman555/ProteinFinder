web: gunicorn ProteinFinder.wsgi
worker: celery -A ProteinFinder worker -l info
release: python manage.py migrate
