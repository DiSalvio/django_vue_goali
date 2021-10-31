"""goali URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.urls import path
from goali_app.views import goali_app_view, add_goal_view, delete_goal_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('goali_app/', goali_app_view),
    path('add_goal/', add_goal_view),
    path('delete_goal/<int:goal_id>/', delete_goal_view)
]
