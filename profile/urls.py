from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^signup', views.signup, name="signup"),
    url(r'^signin', views.signin, name="signin"),
    url(r'^signout', views.signout, name="signout"),
    url(r'^edit', views.edit_profile, name="profile_edit"),
]
