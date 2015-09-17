from . import views
from django.conf.urls import url


urlpatterns = [
    url(r'^signup', views.signup, name="signup"),
    url(r'^signin', views.signin, name="signin"),
    url(r'^signout', views.signout, name="signout"),
    url(r'^edit', views.edit_profile, name="profile_edit"),
    url(r'^forgot_password', views.forgot_password, name="forgot_password"),
    url(r'^reset_password/(?P<uid>[\w]{8}-[\w]{4}-[\w]{4}-[\w]{4}-[\w]{12})/$', views.reset_password, name="reset_password"),
]
