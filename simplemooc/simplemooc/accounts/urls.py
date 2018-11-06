from django.urls import path, include

from django.contrib.auth import views as auth_views
from simplemooc.accounts.views import register, logout_view, dashboard, edit, edit_password, password_reset

app_name = 'accounts'

urlpatterns = [
    #path('entrar/', LoginView,  {'template_name': 'accounts/login.html'}, name="login"),
    path('', dashboard, name='dashboard'),
    path('entrar/', auth_views.LoginView.as_view(), name='login'),
    path('sair/', logout_view, name='logout'),
    path('cadastre-se/', register, name='register'),
    path('nova-senha/', password_reset, name='password_reset'),
    path('editar/', edit, name='edit'),
    path('editar-senha/', edit_password, name='edit_password'),
]