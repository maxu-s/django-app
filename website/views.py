from django.shortcuts import render

def base(request):
    return render(request, 'website/base.html')

def gamemodes(request):
    return render(request, 'website/gamemodes.html')

def ranking(request):
    return render(request, 'website/ranking.html')

def servers(request):
    return render(request, 'website/servers.html')

def tutorials(request):
    return render(request, 'website/tutorials.html')