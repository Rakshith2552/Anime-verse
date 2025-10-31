from django.urls import path
from animeapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('anime/<int:anime_id>/',views.anime_details,name='anime_detail'),
]
