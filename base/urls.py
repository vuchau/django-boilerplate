from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^$', views.homepage, name="homepage"),
    url(r'^signup', views.signup, name="signup"),
    url(r'^signin', views.signin, name="signin"),
    url(r'^signout', views.signout, name="signout"),
    url(r'^dashboard', views.dashboard, name="dashboard"),
    url(r'^test-celery', views.test_celery, name="test_celery"),
]
