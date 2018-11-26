from django.conf.urls import include, url
from django.contrib import admin

from . import views


urlpatterns = [
        url(r'^$', views.home_page),
        url(r'^news/', views.news_page),
        url(r'^portfolio/', views.portfolio_page),
        url(r'^login/', views.login_user),
]
