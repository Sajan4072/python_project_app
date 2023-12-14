from django.urls import path
from . import views

urlpatterns= [
    path('',views.log,name='log'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('register/',views.registerPage,name='register'),
    path('index',views.index,name='index'),
    path('delete/<place_name>/',views.delete_place,name='delete_place')

]