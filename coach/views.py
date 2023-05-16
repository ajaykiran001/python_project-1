from django.shortcuts import render

# Create your views here.
def coach(request):
    return render(request, 'coach/index.html')

def playerlist(request):
    return render(request, 'coach/players.html')