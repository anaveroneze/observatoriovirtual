from . import regbackend
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.home, name="home_url"),
    path('contato/', views.contact, name="contato_url"),
    path('sobre/', views.about, name="sobre_url"),
    path('quemsomos/', views.quemsomos, name="quemsomos_url"),
    path('cluster/', views.cluster, name="cluster_url"),
    path('', include('tabela.urls'), name="tabela_url"), #juntar com o de baixo
    path('experimentos/', views.table, name="experimentos_url"),
    path('imagem/', include('imagem.urls'), name="imagem_url"),
    path('agrupamento/', include('agrupamento.urls'), name='agrupamento_url'),
    path('admin/', admin.site.urls),

    path('accounts/register/', regbackend.MyRegistrationView.as_view(), name='register_custom'),
    path('accounts/', include('registration.backends.default.urls')),
    path('register/complete/', TemplateView.as_view(template_name='registration/registration_complete.html'), name='registration_complete'),
    path('register/closed/', TemplateView.as_view(template_name='registration/registration_closed.html'),
         name='registration_disallowed'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
