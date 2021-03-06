"""peoplesviews URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView
from peoplesviews import views
from poll import views as poll_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         TemplateView.as_view(template_name='home.html'),
         name='home'),
    path('poll/<int:pk>/',
         poll_views.PollMainView.as_view(),
         name='poll'),
    path('poll/<int:pk>/recalculate',
         poll_views.recalculate,
         name='recalculate'),
    path('api/', include('peoplesviews.api_urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-check-login.json',
         views.check_login,
         name='api-check-login'),
    url(r'^v/.*$',
        TemplateView.as_view(template_name='index.html')),
]
