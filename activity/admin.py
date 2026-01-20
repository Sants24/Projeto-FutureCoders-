from django.contrib import admin
from .models import Atividade, Questao, Alternativa

class AlternativaInline(admin.TabularInline):
    model = Alternativa
    extra = 4 # Já mostra 4 campos de resposta prontos

class QuestaoAdmin(admin.ModelAdmin):
    inlines = [AlternativaInline]

admin.site.register(Atividade)
admin.site.register(Questao, QuestaoAdmin)