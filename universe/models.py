from django.db import models

class Galaxia(models.Model):
    NOME_CHOICES = [
        ('FRONT', 'Front-end'),
        ('BACK', 'Back-end'),
    ]
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10, choices=NOME_CHOICES)
    descricao = models.TextField()
    icone = models.ImageField(upload_to='galaxias/', null=True, blank=True)

    def __str__(self):
        return self.nome

class Planeta(models.Model):
    galaxia = models.ForeignKey(Galaxia, on_delete=models.CASCADE, related_name='planetas')
    nome = models.CharField(max_length=50) # Ex: JavaScript, Python
    cor_tema = models.CharField(max_length=7, default='#FFFFFF') 
    icone = models.ImageField(upload_to='planetas/', null=True, blank=True)
    ordem = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nome

class Missao(models.Model):
    planeta = models.ForeignKey(Planeta, on_delete=models.CASCADE, related_name='missoes')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    ordem = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.planeta.nome} - {self.titulo}"