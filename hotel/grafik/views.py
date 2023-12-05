from django.shortcuts import render

def test(request):
    return render(request, 'grafik/index.html')

def gl(request):
    return render(request, 'gowna/glowna.html')