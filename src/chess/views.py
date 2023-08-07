from django.shortcuts import render

from chess.models import User

# Create your views here.
def index(request):
    return render(request, 'chess/index.html')

def info(request):
    users=User.objects.all()
    return render(request, 'chess/info.html',context={"users":users})       #gabarit pour les users
    