from django.urls import path
from menu import views
urlpatterns=[
    path('restro',views.func1,name="p1"),
]