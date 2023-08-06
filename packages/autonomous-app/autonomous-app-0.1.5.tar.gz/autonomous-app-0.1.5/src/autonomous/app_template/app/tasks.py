import time
from celery import shared_task
from autonomous import log
from app import create_app

autotask = create_app().extensions["celery"]


@shared_task()
def taskexample():
    time.sleep(1)
    log.info("MockTask")
    return "success"


@shared_task()
def longmocktask():
    time.sleep(30)
    return "success"


@shared_task()
def parametermocktask(*args, **kwargs):
    log("ParameterMockTask", args, kwargs)
    return "success"


@shared_task()
def errormocktask():
    raise Exception("ErrorMockTask")
