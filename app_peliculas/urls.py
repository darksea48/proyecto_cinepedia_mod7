from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cine/', views.PeliculaListView.as_view(), name='pelicula_list'),
    path('cine/nueva/', views.PeliculaCreateView.as_view(), name='pelicula_create'),
    path('cine/editar/<int:pk>/', views.PeliculaUpdateView.as_view(), name='pelicula_update'),
    path('cine/eliminar/<int:pk>/', views.PeliculaDeleteView.as_view(), name='pelicula_delete'),
    path('cine/<int:pk>/', views.PeliculaDetailView.as_view(), name='pelicula_detail'),
    path('comentario/fijar/<int:comentario_id>/', views.fijar_comentario, name='fijar_comentario'),
    path('comentario/desfijar/<int:comentario_id>/', views.desfijar_comentario, name='desfijar_comentario'),
    path('comentario/eliminar/<int:comentario_id>/', views.comentario_delete, name='comentario_delete'),
]