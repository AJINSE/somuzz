from django.urls import path
from . import views
app_name = 'sports'
urlpatterns = [path('sports/', views.sportss, name='home'),
               path('loop/', views.loop, name='house'),
               path('login/', views.jaya, name='login-page'),
               path('logout/', views.out, name='logout-page'),
               path('register/', views.reg, name='register-page')]
