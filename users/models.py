from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # O avatar do astronauta
    avatar = models.ImageField(upload_to='avatars/', default='default_astronaut.png', null=True, blank=True)

class ProgressoUsuario(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Usamos 'activity.Atividade' entre aspas para evitar erro de carregamento circular
    atividade = models.ForeignKey('activity.Atividade', on_delete=models.CASCADE)
    concluido = models.BooleanField(default=False)
    data_conclusao = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'atividade')