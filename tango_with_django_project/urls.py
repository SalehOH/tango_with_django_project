from django.contrib import admin
from django.urls import path, include
from rango import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('rango/', include('rango.urls'))
]
