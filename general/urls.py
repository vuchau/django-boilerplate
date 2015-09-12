from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.homepage, name="homepage"),
    url(r'^dashboard', views.dashboard, name="dashboard"),
    url(r'^test-celery', views.test_celery, name="test_celery"),
    url(r'^rest', views.rest, name="rest"),
]
