from django.conf.urls import url, include
from rest_framework import routers
from .views.GeoPointView import GeoPointView
from .views.ItineraryView import ItineraryView
from .views.NoteView import NoteView


router = routers.DefaultRouter()
router.register(r'itinerary', ItineraryView)
router.register(r'geopoint', GeoPointView)
router.register(r'note', NoteView)

urlpatterns = [
    url(r'^v1/', include(router.urls)),
]
