from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('pokemons/', views.pokemon_index, name='pokemon-index'),
  path('pokemons/<int:poke_id>/', views.poke_detail, name='poke-detail'),
]