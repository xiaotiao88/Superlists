"""Superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lists.views import home_page
from lists.views import view_list
from lists.views import new_list
from lists.views import add_item


urlpatterns =[
    # Examples:
     url(r'^$',home_page,name='home'),
     url(r'^(\d+)/$',view_list,name='view_list'),
     url(r'^(\d+)/add_item$',add_item,name='add_item'),
     url(r'^new$',new_list,name='new_list'),    
    # url(r'^blog/',include('blog.urls')),
    
    # url(r'^admin/', include(admin.site.urls)),
]
