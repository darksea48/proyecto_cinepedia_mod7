from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from django.shortcuts import get_object_or_404
from .forms import ComentarioForm, PeliculaForm


# Create your views here.
def index(request):
    return render(request, 'index.html')

class PeliculaListView(LoginRequiredMixin, ListView):
    model = Pelicula
    template_name = 'lista.html'
    context_object_name = 'peliculas'


class PeliculaCreateView(LoginRequiredMixin, CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'form.html'
    success_url = reverse_lazy('pelicula_list')
    
    def form_valid(self, form):
        form.instance.publicado_por = self.request.user
        messages.success(self.request, "La película ha sido creada exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrige los errores del formulario.")
        return super().form_invalid(form)

class PeliculaUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'form.html'
    success_url = reverse_lazy('pelicula_list')
    
    def form_valid(self, form):
        messages.success(self.request, "La película ha sido actualizada exitosamente.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Por favor, corrige los errores del formulario.")
        return super().form_invalid(form)
    
    def test_func(self):
        pelicula = self.get_object()
        return self.request.user == pelicula.publicado_por
    
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para editar esta película.")
        return redirect('pelicula_list')

class PeliculaDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pelicula
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('pelicula_list')
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "La película ha sido eliminada exitosamente.")
        return super().delete(request, *args, **kwargs)
    
    def test_func(self):
        pelicula = self.get_object()
        return self.request.user == pelicula.publicado_por
    
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para eliminar esta película.")
        return redirect('pelicula_list')

class PeliculaDetailView(LoginRequiredMixin, DetailView):
    model = Pelicula
    template_name = 'detalle.html'
    context_object_name = 'pelicula'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentario_form'] = ComentarioForm()
        context['comentarios'] = self.object.comentarios.all()
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = Comentario(
                contenido=form.cleaned_data['contenido'],
                pelicula=self.object,
                autor=request.user
            )
            nuevo_comentario.save()
            messages.success(request, "Comentario agregado exitosamente.")
            return redirect('pelicula_detail', pk=self.object.pk)
        else:
            context = self.get_context_data()
            context['comentario_form'] = form
            messages.error(request, "Por favor, corrige los errores del formulario.")
            return self.render_to_response(context)

def fijar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    
    # Verificar si ya hay 2 comentarios fijados
    comentarios_fijados = Comentario.objects.filter(
        pelicula=comentario.pelicula, 
        fijado=True
    ).count()
    
    if comentarios_fijados >= 2:
        messages.error(request, 'No puedes fijar más de 2 comentarios por película. Prueba con desfijar alguno.')
    else:
        comentario.fijado = True
        comentario.save()
        messages.success(request, 'Comentario fijado exitosamente.')
        
    return redirect('pelicula_detail', pk=comentario.pelicula.id)

def desfijar_comentario(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    comentario.fijado = False
    comentario.save()
    messages.success(request, 'Comentario desfijado exitosamente.')
    return redirect('pelicula_detail', pk=comentario.pelicula.id)

def comentario_delete(request, comentario_id):
    comentario = get_object_or_404(Comentario, id=comentario_id)
    if comentario.autor != request.user and comentario.pelicula.publicado_por != request.user:
        messages.error(request, "No tienes permiso para eliminar este comentario.")
        return redirect('pelicula_detail', pk=comentario.pelicula.id)
    
    pelicula_id = comentario.pelicula.id
    comentario.delete()
    messages.success(request, "Comentario eliminado exitosamente.")
    return redirect('pelicula_detail', pk=pelicula_id)