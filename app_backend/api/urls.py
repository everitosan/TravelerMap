from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views.GeoPointView import GeoPointView
from .views.ItineraryView import ItineraryView
from .views.NoteView import NoteView


router = routers.DefaultRouter()
router.register(r'itinerary', ItineraryView)
router.register(r'geopoint', GeoPointView)
router.register(r'note', NoteView)

urlpatterns = [
    url(r'^v1/', include(router.urls)),
    url(r'^docs/', include_docs_urls(title="API documentation"))
]
