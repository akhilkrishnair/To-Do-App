from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home,name="home"),
    path('delete/<int:task_id>/',views.Delete, name="delete"),
    path('update/<int:task_id>/',views.Update, name="update"),
]