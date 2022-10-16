import json

from django.contrib.gis.db.models import Union
from django.contrib.gis.db.models.functions import (
    AsGeoJSON,
    BoundingCircle,
    Centroid,
    Distance,
    Envelope,
)
from django.contrib.gis.measure import D
from django.core.serializers import serialize
from django.db.models import Q
from django.shortcuts import render
from geojson import Feature
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_gis.filters import DistanceToPointFilter, InBBoxFilter
from rest_framework_gis.pagination import GeoJsonPagination
from world.models import AdminiBoundary, Airport
from world.serializers import AdminiBoundarySerializer, AirportSerializer


class AirportAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            airport_name = self.request.GET.get("name", "新千歳空港")
            airports = Airport.objects.filter(c28_005=airport_name)
            serializer = AirportSerializer(airports, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class IntersectsAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__intersects=airport.geom)
            serializer = AdminiBoundarySerializer(target_admini_boundary, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class CrossesAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__crosses=airport.geom)

            serializer = AdminiBoundarySerializer(target_admini_boundary, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class ContainsAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__contains=airport.geom)

            serializer = AdminiBoundarySerializer(target_admini_boundary, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class WithinAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__within=airport.geom)

            serializer = AdminiBoundarySerializer(target_admini_boundary, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class OverlapsAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__overlaps=airport.geom)

            data = serialize("geojson", target_admini_boundary)
            result = json.loads(data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class DisjointAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__disjoint=airport.geom)

            data = serialize("geojson", target_admini_boundary)
            result = json.loads(data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class TouchesAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__touches=airport.geom)

            data = serialize("geojson", target_admini_boundary)
            result = json.loads(data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class LeftAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__left=airport.geom)

            data = serialize("geojson", target_admini_boundary)
            result = json.loads(data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class RightAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__right=airport.geom)

            data = serialize("geojson", target_admini_boundary)
            result = json.loads(data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class OverlapsAboveAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__overlaps_above=airport.geom)

            data = serialize("geojson", target_admini_boundary)
            result = json.loads(data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class OverlapsBelowAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__overlaps_below=airport.geom)

            data = serialize("geojson", target_admini_boundary)
            result = json.loads(data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class DistanceGtAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__distance_gt=(airport.geom, D(km=100)))

            data = serialize("geojson", target_admini_boundary)
            result = json.loads(data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class DistanceGteAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__distance_gte=(airport.geom, D(km=100)))

            data = serialize("geojson", target_admini_boundary)
            result = json.loads(data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class DistanceLtAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__distance_lt=(airport.geom, D(km=100)))

            data = serialize("geojson", target_admini_boundary)
            result = json.loads(data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class DistanceLteAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__distance_lte=(airport.geom, D(km=100)))

            data = serialize("geojson", target_admini_boundary)
            result = json.loads(data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class DwithinAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airport_name = self.request.GET.get("airport", "新千歳空港")
            airport = Airport.objects.filter(c28_005=airport_name).first()
            target_admini_boundary = admini_boundary.filter(geom__dwithin=(airport.geom, 1))

            data = serialize("geojson", target_admini_boundary)
            result = json.loads(data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class UnionAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            admini_boundary = AdminiBoundary.objects.filter(
                Q(n03_003__isnull=False) | Q(n03_004__isnull=False), n03_002__isnull=False
            )

            airports = Airport.objects.aggregate(Union("geom"))
            target_admini_boundary = admini_boundary.filter(geom__intersects=airports["geom__union"])

            data = serialize("geojson", target_admini_boundary)
            result = json.loads(data)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class AsGeoJSONAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            airport_name = self.request.GET.get("airport", "新千歳空港")

            # レコードのフィールドからpropertiesを取得しておく
            properties = Airport.objects.filter(c28_005=airport_name).values()[0]
            del properties["geom"]

            geom = Airport.objects.annotate(json=AsGeoJSON("geom")).filter(c28_005=airport_name).first().json
            # GeoJSONの型にする
            result = Feature(geometry=json.loads(geom), properties=properties)
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class CentroidAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            airport_name = self.request.GET.get("airport", "新千歳空港")
            geom = Airport.objects.annotate(json=AsGeoJSON(Centroid("geom"))).filter(c28_005=airport_name).first().json
            result = Feature(geometry=json.loads(geom))
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class BouidingCircleAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            airport_name = self.request.GET.get("airport", "新千歳空港")
            geom = (
                Airport.objects.annotate(json=AsGeoJSON(BoundingCircle("geom")))
                .filter(c28_005=airport_name)
                .first()
                .json
            )
            result = Feature(geometry=json.loads(geom))
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class EnvelopeAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            airport_name = self.request.GET.get("airport", "新千歳空港")
            geom = Airport.objects.annotate(json=AsGeoJSON(Envelope("geom"))).filter(c28_005=airport_name).first().json
            result = Feature(geometry=json.loads(geom))
            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class DistanceAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            airport_name = self.request.GET.get("airport", "新千歳空港")
            new_chitose = Airport.objects.filter(c28_005="新千歳空港").first()
            distance = (
                Airport.objects.annotate(distance=Distance("geom", new_chitose.geom, spheroid=True))
                .filter(c28_005=airport_name)
                .first()
                .distance
            )
            return Response({"value": f"新千歳空港からの距離は{distance.standard}mです"}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class CentroidLngLatAPIView(APIView):
    def get(self, request, *args, **keywords):
        try:
            airport_name = self.request.GET.get("airport", "新千歳空港")
            geom = Airport.objects.annotate(json=AsGeoJSON(Centroid("geom"))).filter(c28_005=airport_name).first().json
            return Response({"lnglat": json.loads(geom)["coordinates"]}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({}, status=status.HTTP_404_NOT_FOUND)


class AirportPagination(GeoJsonPagination):
    page_size_query_param = "page_size"


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    pagination_class = AirportPagination
    filter_backends = (DistanceToPointFilter, InBBoxFilter)
    distance_filter_field = "geom"
    bbox_filter_field = "geom"
    bbox_filter_include_overlapping = True


def index(request):
    contexts = {}
    return render(request, "world/index.html", contexts)
