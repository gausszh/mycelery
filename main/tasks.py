# coding=utf8
# from celery import shared_task
from celery.task import task
import requests


@task()
def document_length(p):
    """
    get url document, cal size
    """
    url = "http://baidu.com"
    print url
    ret = requests.get(url)
    import time
    print p
    time.sleep(20)
    print ret.content[:100]
    return len(ret.content)
