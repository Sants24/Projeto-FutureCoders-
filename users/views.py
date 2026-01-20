from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        # Pega os dados que o usuário digitou
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('lista_galaxias') # Manda para a tela nova
        else:
            messages.error(request, "Usuário ou senha inválidos!")
    
    return render(request, 'login.html')