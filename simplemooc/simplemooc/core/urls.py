from django.urls import path, include

from simplemooc.core.views import home
from simplemooc.core.views import contact

app_name = 'core'

urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name="contact"),
]