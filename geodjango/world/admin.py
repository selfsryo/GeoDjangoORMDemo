from django.contrib.gis import admin
from world.models import AdminiBoundary, Airport

admin.site.register(Airport, admin.GeoModelAdmin)
admin.site.register(AdminiBoundary, admin.GeoModelAdmin)
