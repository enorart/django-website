from django.shortcuts import render

from datetime import datetime

from chess.models import User

def index(request):
    date=datetime.now()
    return render(request, 'Site/index.html',context={"date":date})

def about(request):
    return render(request, 'Site/about.html')

