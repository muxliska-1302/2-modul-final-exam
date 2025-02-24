from django.shortcuts import render
from .models import Subject
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from .forms import SubjectForm


class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/list.html'
    context_object_name = 'subjects'

    def get_queryset(self):
        queryset = Subject.objects.all()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        department_filter = self.request.GET.get('department')
        if department_filter:
            queryset = queryset.filter(department__name=department_filter)
        grade_filter = self.request.GET.get('grade')
        if grade_filter:
            queryset = queryset.filter(grade=grade_filter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Subject.objects.values_list('department__name', flat=True).distinct()
        context['grades'] = Subject.objects.values_list('grade', flat=True).distinct()
        return context

class SubjectCreateView(CreateView):
    model = Subject
    template_name = 'subjects/form.html'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects:list')

class SubjectUpdateView(UpdateView):
    model = Subject
    template_name = 'subjects/form.html'
    form_class = SubjectForm
    success_url = reverse_lazy('subjects:list')
    context_object_name = 'subject'

class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'subjects/detail.html'
    context_object_name = 'subject'

class SubjectDeleteView(DeleteView):
    model = Subject
    success_url = reverse_lazy('subjects:list')
    context_object_name = 'subject'
