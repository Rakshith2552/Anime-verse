from django.urls import path
from animeapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('anime/<int:anime_id>/',views.anime_details,name='anime_detail'),
    path('add-to-watchlist/<int:anime_id>/',views.add_to_watchlist,name='add_to_watchlist'),
    path('watchlist/',views.watchlist,name='watchlist'),
]
