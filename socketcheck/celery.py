
import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socketcheck.settings')
# Create the Celery app
app = Celery('socketcheck')
# Load the Celery config from the Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')
# Discover tasks in all installed Django apps
app.autodiscover_tasks()
@app.task(bind=True)


def debug_task(self):
    print(f'Request: { self.request!r}') 
        