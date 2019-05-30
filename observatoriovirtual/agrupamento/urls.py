from django.urls import path
from . import views

app_name = 'agrupamento'
urlpatterns = [
    path('', views.about, name="agrupamento_url"),
    path('agrupamento/', views.fof, name="fof_url"),
]
