
from django.contrib import admin
from django.urls import path
from app1 import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('explore/', views.explore_more, name='explore'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('create/', views.post_create, name='post_create'),
    path('post/<int:pk>/update/', views.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('register/', views.register, name='register'),  # ✅ add this
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)