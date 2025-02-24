from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
    path('students-list/', views.StudentListView.as_view(), name='list'),
    path('student-create/', views.StudentCreateView.as_view(), name='create'),
    path('student-update/<int:pk>/', views.StudentUpdateView.as_view(), name='update'),
    path('student-detail/<int:pk>/', views.StudentDetailView.as_view(), name='detail'),
    path('student-delete/<int:pk>/', views.StudentDeleteView.as_view(), name='delete'),
]