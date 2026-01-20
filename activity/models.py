from django.db import models
from universe.models import Missao

class Atividade(models.Model):
    TIPO_CHOICES = [
        ('TEORIA', 'Teoria'),
        ('QUIZ', 'Exercício'),
    ]
    missao = models.ForeignKey(Missao, on_delete=models.CASCADE, related_name='atividades')
    titulo = models.CharField(max_length=150)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    conteudo_teorico = models.TextField(blank=True, null=True) # Pode ser HTML
    ordem = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo

class Questao(models.Model):
    # Relacionamento 1 para 1: Uma atividade do tipo QUIZ tem UMA questão
    atividade = models.OneToOneField(Atividade, on_delete=models.CASCADE, related_name='questao')
    enunciado = models.TextField()
    explicacao_erro = models.TextField(help_text="Texto para o feedback de erro")
    explicacao_acerto = models.TextField(help_text="Texto para o feedback de acerto")

    def __str__(self):
        return self.enunciado[:50]

class Alternativa(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE, related_name='alternativas')
    texto = models.CharField(max_length=200)
    is_correta = models.BooleanField(default=False)

    def __str__(self):
        return self.texto