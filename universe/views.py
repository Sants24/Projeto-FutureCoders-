from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Galaxia

@login_required # Só deixa entrar se estiver logado
def lista_galaxias(request):
    galaxias = Galaxia.objects.all()
    return render(request, 'galaxias.html', {'galaxias': galaxias})