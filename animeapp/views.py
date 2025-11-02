from django.shortcuts import render,redirect
from animeapp.models import Watchlist
import requests

# Create your views here.
def home(request):
    query=request.GET.get('q')
    results=[]
    
    if query:
        url=f'https://api.jikan.moe/v4/anime?q={query}&limit=20'
        response=requests.get(url)
        if response.status_code==200:
            data=response.json()
            results=data.get('data',[])
    return render(request,'home.html',{'results':results,'query':query})


def anime_details(request,anime_id):
    url=f'https://api.jikan.moe/v4/anime/{anime_id}/full'
    response=requests.get(url)
    anime=None
    
    if response.status_code==200:
        data=response.json()
        anime=data.get('data',None)
    else:
        print("Error fetching anime details")
    
    return render(request,'anime_detail.html',{'anime':anime})

def add_to_watchlist(request, anime_id):
    try:
        url = f'https://api.jikan.moe/v4/anime/{anime_id}/full'
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            data = response.json().get('data', {})

            title = data.get('title', 'Unknown Title')
            image_url = data.get('images', {}).get('jpg', {}).get('image_url', '')
            score = data.get('score', None)

            if not image_url:
                image_url = "https://via.placeholder.com/300x400?text=No+Image"

            # Prevent duplicates
            obj, created = Watchlist.objects.get_or_create(
                anime_id=anime_id,
                defaults={'title': title, 'image_url': image_url, 'score': score}
            )
            if created:
                print(f"✅ Added to watchlist: {title}")
            else:
                print("ℹ️ Already in watchlist:", title)
        else:
            print("❌ API returned:", response.status_code)
    except Exception as e:
        print("⚠️ Error adding to watchlist:", e)

    return redirect('watchlist')
# def watchlist(request):
#     animes=Watchlist.objects.all().order_by('-added_at')
#     return render(request,'watchlist.html',{'animes':animes})


def watchlist(request):
    try:
        animes = Watchlist.objects.all().order_by('-added_at')
        print(f"🎬 Loaded watchlist ({len(animes)} items)")
        return render(request, 'watchlist.html', {'animes': animes})
    except Exception as e:
        print("⚠️ Error loading watchlist:", e)
        return render(request, 'watchlist.html', {'animes': []})
