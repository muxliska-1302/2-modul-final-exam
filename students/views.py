from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Student
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from students.forms import StudentForm


class StudentListView(ListView):
    model = Student
    template_name = 'students/list.html'
    context_object_name = 'students'

    def get_queryset(self):
        queryset = Student.objects.all()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(first_name__icontains=search_query) | queryset.filter(
                last_name__icontains=search_query)
        grade_filter = self.request.GET.get('grade')
        if grade_filter:
            queryset = queryset.filter(grade=grade_filter)
        group_filter = self.request.GET.get('group')
        if group_filter:
            queryset = queryset.filter(group__name=group_filter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['grades'] = Student.objects.values_list('grade', flat=True).distinct()
        context['groups'] = Student.objects.values_list('group__name', flat=True).distinct()
        return context

class StudentCreateView(CreateView):
    model = Student
    template_name = 'students/form.html'
    form_class = StudentForm
    success_url = reverse_lazy('students:list')

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'students/form.html'
    form_class = StudentForm
    success_url = reverse_lazy('students:list')
    context_object_name = 'student'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/detail.html'
    context_object_name = 'student'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    context_object_name = 'student'
