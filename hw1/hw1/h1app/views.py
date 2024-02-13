# Создайте пару представлений в вашем первом приложении:
# — главная
# — о себе.
# Внутри каждого представления должна быть переменная html —
# многострочный текст с HTML-вёрсткой и данными о вашем первом Django-сайте и о вас.
# Сохраняйте в логи данные о посещении страниц.

from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def main(request):
    logging.info("main page reached")
    html = """<h1>Main page</h1><br>
    <p>This page is dedicated to my first Django-app.</p>
    <p>lorem20</p>"""
    return HttpResponse(html)

def about(request):
    logging.info("about page reached")
    html = """<h1>About me</h1><br>
    <p>My name is Anna. I love coding</p>
    <p>lorem20</p><br>
    <p>lorem20</p>"""
    return HttpResponse(html)