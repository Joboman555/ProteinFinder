from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProteinFinder.settings')
app = Celery('ProteinFinder')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

broker_url = os.environ['REDIS_URL'] if 'REDIS_URL' in os.environ else 'redis://localhost:6379'
celery_result_backend = os.environ['REDIS_URL'] if 'REDIS_URL' in os.environ else  'redis://localhost:6379'
app.conf.update(BROKER_URL=broker_url,
                CELERY_RESULT_BACKEND=celery_result_backend)



@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))