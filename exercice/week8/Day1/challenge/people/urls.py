from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.people, name='people')
    
   # path('<people/int:id>/', views.people_one, name='people')
]