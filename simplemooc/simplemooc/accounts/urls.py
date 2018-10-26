from django.urls import path, include

from django.contrib.auth import views as auth_views
from simplemooc.accounts.views import register

app_name = 'accounts'

urlpatterns = [
    #path('entrar/', LoginView,  {'template_name': 'accounts/login.html'}, name="login"),
    path('entrar/', auth_views.LoginView.as_view(), name='login'),
    path('cadastre-se/', register, name='register'),
]