
from celery import Celery

from celery import platforms

from celery_tasks import celery_config


platforms.C_FORCE_ROOT = True

celery2 = Celery('celery_tasks')
celery2.config_from_object(celery_config)

def main1(id):
    from celery_tasks.task1 import t1
    from celery_tasks.task2 import t2
    t1.apply_async((id,))
    t2.apply_async((id,))





