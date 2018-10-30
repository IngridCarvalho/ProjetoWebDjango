from django.urls import path, include

from django.contrib.auth import views as auth_views
from simplemooc.accounts.views import register, logout_view, dashboard, edit

app_name = 'accounts'

urlpatterns = [
    #path('entrar/', LoginView,  {'template_name': 'accounts/login.html'}, name="login"),
    path('', dashboard, name='dashboard'),
    path('entrar/', auth_views.LoginView.as_view(), name='login'),
    path('sair/', logout_view, name='logout'),
    path('cadastre-se/', register, name='register'),
    path('editar/', edit, name='edit'),
]