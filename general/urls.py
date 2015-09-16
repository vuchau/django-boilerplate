from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.homepage, name="homepage"),
    url(r'^dashboard', views.dashboard, name="dashboard"),
    url(r'^rest', views.rest, name="rest"),
]
