from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
urlpatterns = [
    path('login',views.login_user,name="login_user"),
    path('register',views.register_user,name="register_user")
]
urlpatterns += staticfiles_urlpatterns()