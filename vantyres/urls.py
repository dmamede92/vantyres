"""
    @author: David Mamede
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('profiles.urls')),
    path('', include('clients.urls')),
    path('', include('brands.urls'))
]
