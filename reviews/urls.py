from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('api/items/', views.item_api_list, name='item_api_list'), 
    path('api/items/<int:pk>/', views.item_api_detail, name='item_api_detail'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='reviews/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search/', views.search, name='search'),
]