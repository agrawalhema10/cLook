from django.urls import path
from . import views
urlpatterns = [
    path('',views.p_login,name='p_login'),
    path('profile',views.profile,name='profile'),
    path('p_log',views.p_log,name='p_log'),
    path('profo',views.profo,name='profo')
]