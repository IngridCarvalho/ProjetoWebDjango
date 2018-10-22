from django.urls import path, include

from django.contrib.auth import login

app_name = 'login'

urlpatterns = [
    path('entrar', login, {'template_name':'login.html'}, name="login"),
]