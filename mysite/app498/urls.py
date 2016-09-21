# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.ListHistoryView.as_view(), name='list'),
    url(r'^add/$', views.CreateHistoryView.as_view(), name='add'),
]
