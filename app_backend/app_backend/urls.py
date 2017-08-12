from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('api.urls'))
]
