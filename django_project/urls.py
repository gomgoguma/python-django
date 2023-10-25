from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', include('test_app.urls')),
    path('', include('api.urls')),
    path('auth/', include('my_auth.urls'))
]
