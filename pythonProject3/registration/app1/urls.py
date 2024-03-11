from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home-view'),
    path('login', views.login_view, name='login-view'),
    path('signup', views.signup_view, name='sign-view'),

    # other paths in your app
]