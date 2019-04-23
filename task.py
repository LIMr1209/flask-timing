# 异步执行调用函数

from apscheduler.schedulers.background import BackgroundScheduler
from config import executors, jobstores

scheduler = BackgroundScheduler(executors=executors, jobstores=jobstores)
scheduler.daemonic = False
scheduler.start()
