from django.shortcuts import render
from .models import Teacher
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import TeacherForm


class TeacherListView(ListView):
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teachers'

class TeacherCreateView(CreateView):
    model = Teacher
    template_name = 'teachers/form.html'
    form_class = TeacherForm
    success_url = reverse_lazy('teachers:list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    template_name = 'teachers/form.html'
    form_class = TeacherForm
    success_url = reverse_lazy('teachers:list')
    context_object_name = 'teacher'

    def get_queryset(self):
        queryset = Teacher.objects.all()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(first_name__icontains=search_query) | queryset.filter(
                last_name__icontains=search_query)
        department_filter = self.request.GET.get('department')
        if department_filter:
            queryset = queryset.filter(department__name=department_filter)
        subject_filter = self.request.GET.get('subject')
        if subject_filter:
            queryset = queryset.filter(subjects__name=subject_filter).distinct()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Teacher.objects.values_list('department__name', flat=True).distinct()
        context['subjects'] = Teacher.objects.values_list('subjects__name', flat=True).distinct()
        return context

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'teachers/detail.html'
    context_object_name = 'teacher'

class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('teachers:list')
    context_object_name = 'teacher'