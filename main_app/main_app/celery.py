import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_app.settings')

app = Celery('main_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# celery beat tasks

app.conf.beat_schedule = {
    'send-spam-every-1-min':
        {
            'task': 'send_email.tasks.send_beat_email',  # name directory application and send_beat_email - name tasks
            'schedule': crontab(minute='*/1'),  # period send
        },
}
