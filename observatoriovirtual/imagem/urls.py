from django.urls import path
from . import views

app_name = 'imagem'
urlpatterns = [
    path('', views.about, name="imagem_url"),
    path('wavelet', views.wavelet, name="wavelet_url")
    ]
