"""
Конфигурация URL-адреса для проекта ZeroCoder.

Список `urlpatterns` направляет URL-адреса в представления.
Для получения дополнительной информации см.:
 https://docs.djangoproject.com/en/5.0/topics/http/urls/
Примеры:
Представления функций
 1. Добавляя импорт:
from my_app import views
 2. Добавьте URL-адрес в urlpatterns:
 path('',views.home, name='home')
Представления на основе классов
 1. Добавляя импорт:
from other_app.views import Home
 2. Добавьте URL-адрес в urlpatterns: path('', Home.as_view(), name='home')
Включение другого URLconf
 1. Импортируя функцию include():
from django.urls import include, path
 2. Добавьте URL-адрес в urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls'))
]
