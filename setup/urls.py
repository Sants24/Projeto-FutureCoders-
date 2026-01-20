from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Importe as views
from users.views import login_view
from universe.views import lista_galaxias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    
    # Nova rota:
    path('galaxias/', lista_galaxias, name='lista_galaxias'),
]

# Isso permite carregar as imagens (ícones) que você upar
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)