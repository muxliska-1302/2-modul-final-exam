from django.urls import path
from . import views


app_name = 'teachers'

urlpatterns = [
    path('teachers-list/', views.TeacherListView.as_view(), name='list'),
    path('teachers-create/', views.TeacherCreateView.as_view(), name='create'),
    path('teacher-update/<int:pk>/', views.TeacherUpdateView.as_view(), name='update'),
    path('teacher-detail/<int:pk>/', views.TeacherDetailView.as_view(), name='detail'),
    path('teacher-delete/<int:pk>/', views.TeacherDeleteView.as_view(), name='delete'),
]