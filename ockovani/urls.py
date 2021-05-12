from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('seznamvakcin/', views.seznamvakcin, name='seznam_vakcin'),
    path('ockovani/', views.OckovaniListView.as_view(), name='ockovani'),
    path('ockovani/vakciny/<str:vakcina_nazev_firmy>/', views.OckovaniListView.as_view(), name='vakcina_genre'),
    path('ockovani/<int:pk>/', views.OckovaniDetailView.as_view(), name='osoba_detail'),
]