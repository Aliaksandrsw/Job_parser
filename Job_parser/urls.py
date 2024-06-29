
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scraping.urls')),
    path('users/', include('users.urls', namespace='users')),
    path("api/", include("scraping_api.urls")),
    path("api-auth/", include("rest_framework.urls")),
]
