from autonomous import log
from app.tasks import mocktask, longmocktask, parametermocktask, errormocktask
import time
from celery.result import AsyncResult
import pytest


def test_base_task(app):
    results = mocktask.delay()
    # breakpoint()
    results.ready()
    while not results.ready():
        time.sleep(1)
        log(results.status)
    assert results.get() == "success"


def test_base_long_task(app):
    task = longmocktask.delay()
    result = AsyncResult(task.id)
    log(result.status)
    result.ready()
    assert result.get() == "success"


def test_param_task(app):
    results = parametermocktask.delay("hello", "world", key="value")
    while not results.ready():
        time.sleep(1)
        log(results.status)
    assert results.get() == "success"


def test_error_task(app):
    try:
        results = errormocktask.delay()
    except Exception as e:
        log(e)

    while not results.ready():
        time.sleep(1)
        log(results.status)
    assert results.get() == "success"
