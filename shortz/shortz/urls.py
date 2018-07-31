from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from shortener import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('shorten_url/', views.shorten_url),
    path('<code>', views.resolve_to_full_url)
]
