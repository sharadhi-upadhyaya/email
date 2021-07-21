from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('login/create',views.create,name='create'),
    path('login/message',views.message,name='message'),
]
