from django.shortcuts import render
from .models import *

def INDEX(request):
    return render(request,'user/index.html')
