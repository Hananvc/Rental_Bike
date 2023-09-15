from django.urls import path
from .import views



urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('inventory/', views.inventory, name='inventory'),
    path('adminpanel/', views.adminpanel , name='adminpanel'),
    path('adminedit/', views.adminedit , name='adminedit'),
    path('<int:id>/',views.updateuser,name='updateuser'),
    path('deleteuser/<int:id>/', views.deleteuser, name='deleteuser'),
    path('search_username/',views.SearchName,name='search_username')

]

