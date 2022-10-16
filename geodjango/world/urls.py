from django.urls import include, path
from rest_framework import routers
from world import views
from world.views import AirportViewSet

router = routers.DefaultRouter()
router.register("", AirportViewSet)

urlpatterns = [
    path("airport/", views.AirportAPIView.as_view(), name="airport"),
    path("intersects/", views.IntersectsAPIView.as_view(), name="intersects"),
    path("crosses/", views.CrossesAPIView.as_view(), name="crosses"),
    path("contains/", views.ContainsAPIView.as_view(), name="contains"),
    path("within/", views.WithinAPIView.as_view(), name="within"),
    path("overlaps/", views.OverlapsAPIView.as_view(), name="overlaps"),
    path("disjoint/", views.DisjointAPIView.as_view(), name="disjoint"),
    path("touches/", views.TouchesAPIView.as_view(), name="touches"),
    path("left/", views.LeftAPIView.as_view(), name="left"),
    path("right/", views.RightAPIView.as_view(), name="right"),
    path("overlaps_above/", views.OverlapsAboveAPIView.as_view(), name="overlaps_above"),
    path("overlaps_below/", views.OverlapsBelowAPIView.as_view(), name="overlaps_below"),
    path("distance_gt/", views.DistanceGtAPIView.as_view(), name="distance_gt"),
    path("distance_gte/", views.DistanceGteAPIView.as_view(), name="distance_gte"),
    path("distance_lt/", views.DistanceLtAPIView.as_view(), name="distance_lt"),
    path("distance_lte/", views.DistanceLteAPIView.as_view(), name="distance_lte"),
    path("dwithin/", views.DistanceLteAPIView.as_view(), name="dwithin"),
    path("union/", views.UnionAPIView.as_view(), name="union"),
    path("asgeojson/", views.AsGeoJSONAPIView.as_view(), name="asgeojson"),
    path("centroid/", views.CentroidAPIView.as_view(), name="centroid"),
    path("boundingcircle/", views.BouidingCircleAPIView.as_view(), name="boundingcircle"),
    path("envelope/", views.EnvelopeAPIView.as_view(), name="envelope"),
    path("distance/", views.DistanceAPIView.as_view(), name="distance"),
    path("centroid_lnglat/", views.CentroidLngLatAPIView.as_view(), name="centroid_lnglat"),
    path("drf_gis_airport/", include(router.urls)),
]
