from django.urls import path
from animeapp import views

urlpatterns = [
    path('',views.home,name='home'),
]
