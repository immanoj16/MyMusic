from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'(?P<band_id>\d+)/$', views.band)
]