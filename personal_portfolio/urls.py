"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static #добавляет новый url шаблон под названием static
from django.conf import settings #передаем в static  объявленные переменные из settings.py
from portfolio import views

urlpatterns = [
    path('',views.home, name='home'), #создание пути к домашней странице
    path('admin/', admin.site.urls), #создание пути к странице админа
    path('blog/', include('blog.urls')), #перенаправление любого запроса с сайта содержащие blog/ на приложение блога
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #теперь у админа во вкладке Project открываются изображения
