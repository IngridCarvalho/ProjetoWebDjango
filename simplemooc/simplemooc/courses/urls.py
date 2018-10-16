from django.urls import path, include

from simplemooc.courses.views import index

app_name = 'index'

urlpatterns = [
    path('', index, name="index"),
]