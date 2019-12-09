"""automation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from RPAPanel import views

router = DefaultRouter()
router.register(r'nodes', views.NodeViewSet)
router.register(r'hubs', views.HubViewSet)

admin.site.site_header = "RPA Automation Admin"
admin.site.site_title = "RPA Automation Portal"
admin.site.index_title = "Welcome to RPA Automation Portal"

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', admin.site.urls),
    url(r'^Nodes/', views.index),
    path('createnode/', views.addnode, name='createnode'),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),

    url(r'^hubs/', views.indexhub),
    path('createhub/', views.addhub, name='createhub'),

    url(r'^process/', views.indexprocess),
    path('createprocess/', views.addprocess, name='createprocess'),
    url(r'^api/', include(router.urls))
]



