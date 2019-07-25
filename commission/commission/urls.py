from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    url(r'^auth/', obtain_jwt_token),
    url(r'^refresh-token/', refresh_jwt_token),
]
