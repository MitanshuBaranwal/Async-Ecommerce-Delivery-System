from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')

app = Celery('ecommerce_project')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')
# Use Redis as the message broker
app.conf.broker_url = 'redis://localhost:6379/0'

# Use Redis as the message broker
# Load task modules from all registered Django app configs.
app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()
@app.task(bind= True)
def debug_task(self):
    print(f'Request: {self.request!r}')