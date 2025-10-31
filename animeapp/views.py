from django.shortcuts import render
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