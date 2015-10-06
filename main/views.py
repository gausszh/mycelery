import logging
from django.shortcuts import render
from django.http import HttpResponse
from cacheback.decorators import cacheback
from main.tasks import document_length

logger = logging.getLogger("")
# Create your views here.

def celery_task(request):
    # url = "https://www.baidu.com"
    # t = document_length.delay(request.GET.get("tt"))
    # print t, type(t)
    t = "request views"
    logger.debug("debug, %s, %s", t, logger)
    logger.info("info, %s, %s", t, logger)

    t = _request_html_url()
    print t
    return HttpResponse(t[30:])


@cacheback(3)
def _request_html_url():
    url = "https://www.baidu.com"
    import requests
    r = requests.get(url)
    import time
    time.sleep(5)
    t = r.content[:100]
    logger.debug("debug, %s, %s", t, logger)
    logger.info("info, %s, %s", t, logger)

    return t