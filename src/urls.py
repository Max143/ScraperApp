from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('website/', include('scraper.urls')),
    path('website/auth/', include('users.urls')),
]
                    