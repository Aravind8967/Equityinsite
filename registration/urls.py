from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('signup/', views.signup_page, name="signup")
]
