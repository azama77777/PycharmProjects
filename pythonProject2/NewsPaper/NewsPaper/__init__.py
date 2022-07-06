from .celery import app as celery_app
from celery import shared_task

from celery import shared_task
import time

@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")

__all__ = ('celery_app',)