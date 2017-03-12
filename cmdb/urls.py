# -*- coding: utf-8 -*-
"""
urls config
"""
from django.conf.urls import patterns, include, url
from django.http.response import HttpResponse


def hello(request):
    return HttpResponse('Hello world')


urlpatterns = patterns(
    url(r'^$', hello)
)


