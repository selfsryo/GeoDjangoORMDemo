from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from world.views import index


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/world/", include("world.urls")),
    path("", index, name='world_index'),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]