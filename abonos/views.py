# Django
from django.shortcuts import render


# Create your views here.
def listar_abonos(request):
    return render(request, 'feed.html')