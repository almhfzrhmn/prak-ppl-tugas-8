from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produk/', include('produk.urls')),
    path('', include('produk.urls')),
]
