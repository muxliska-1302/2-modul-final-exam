from django.urls import path
from . import views


app_name = 'subjects'

urlpatterns = [
    path('subjects-list/', views.SubjectListView.as_view(), name='list'),
    path('subject-create/', views.SubjectCreateView.as_view(), name='create'),
    path('subject-update/<int:pk>/', views.SubjectUpdateView.as_view(), name='update'),
    path('subject-detail/<int:pk>/', views.SubjectDetailView.as_view(), name='detail'),
    path('subject-delete/<int:pk>/', views.SubjectDeleteView.as_view(), name='delete'),
]