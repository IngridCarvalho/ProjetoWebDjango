from django.urls import path, include

from simplemooc.courses.views import index, details

app_name = 'courses'

urlpatterns = [
    path('', index, name="index"),
    #path('<int:pk>/', details, name="details"),
    path('<slug:slug>/', details, name="details"),
]