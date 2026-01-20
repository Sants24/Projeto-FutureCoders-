from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ProgressoUsuario

# Registra o usuário customizado
admin.site.register(CustomUser, UserAdmin)
admin.site.register(ProgressoUsuario)