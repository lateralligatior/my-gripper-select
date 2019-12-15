# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:21:24 2019

@author: Nathan Hilbrands
"""

from django.urls import path
from . import views
urlpatterns = [
        path('', views.post_list, name = 'post_list')
        ]