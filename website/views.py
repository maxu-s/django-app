from django.shortcuts import render

def base(request):
    return render(request, 'website/base.html')

def about(request):
    return render(request, 'website/about.html')

def download(request):
    return render(request, 'website/download.html')

def servers(request):
    return render(request, 'website/servers.html')

def tutorials(request):
    return render(request, 'website/tutorials.html')
