from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from blog.views import index, register

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
    path('api/register/', register),
    path('api/', include('blog.urls')),
]
