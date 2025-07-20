from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get/', views.get, name='get_task'),
    path('api/post/', views.post, name='post_task'),
    path('api/update/', views.update, name='update_task'),
    path('api/delete/', views.delete, name='delete_task'),
]
