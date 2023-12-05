from django.shortcuts import render, HttpResponse

def gl(request):
    return render(request, 'glowna/glowna.html')