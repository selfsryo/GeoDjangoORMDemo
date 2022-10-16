from rest_framework_gis.serializers import GeoFeatureModelSerializer
from world.models import AdminiBoundary, Airport


class AirportSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Airport
        geo_field = "geom"
        auto_bbox = True
        fields = ("c28_005", "geom")


class AdminiBoundarySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = AdminiBoundary
        geo_field = "geom"
        auto_bbox = True
        fields = "__all__"
