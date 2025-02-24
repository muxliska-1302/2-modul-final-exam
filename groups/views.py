from django.shortcuts import render
from .models import Group
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from .forms import GroupForm
from django.urls import reverse_lazy


class GroupListView(ListView):
    model = Group
    template_name = 'groups/list.html'
    context_object_name = 'groups'

    def get_queryset(self):
        queryset = Group.objects.all()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        teacher_filter = self.request.GET.get('teacher')
        if teacher_filter:
            queryset = queryset.filter(teacher__first_name=teacher_filter)
        grade_filter = self.request.GET.get('grade')
        if grade_filter:
            queryset = queryset.filter(grade=grade_filter)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = Group.objects.values_list('teacher__first_name', flat=True).distinct()
        context['grades'] = Group.objects.values_list('grade', flat=True).distinct()
        return context

class GroupCreateView(CreateView):
    model = Group
    template_name = 'groups/form.html'
    form_class = GroupForm
    success_url = reverse_lazy('groups:list')

class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'groups/form.html'
    form_class = GroupForm
    success_url = reverse_lazy('groups:list')
    context_object_name = 'group'

class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'
    context_object_name = 'group'

class GroupDeleteView(DeleteView):
    model = Group
    success_url = reverse_lazy('groups:list')
    context_object_name = 'group'