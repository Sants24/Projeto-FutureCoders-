from django.contrib import admin
from django.urls import path
from users.views import login_view # Importe a view que acabamos de criar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'), # A rota vazia '' será a tela de login
]