from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.police_login,name='police_login'),
    path('police_home',views.police_home,name="police_home"),
    path('add_criminal',views.add_criminal,name="add_criminal"),
    path('add',views.add,name='add'),
    path('new_home',views.new_home,name="new_home"),
    path('search',views.search,name="search"),
    path('search_criminal',views.search_criminal,name="search_criminal")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)