from django.urls import path
from . import views


app_name = 'departments'

urlpatterns = [
    path('departments-list/', views.DepartmentListView.as_view(), name='list'),
    path('department-create/', views.DepartmentCreateView.as_view(), name='create'),
    path('department-update/<int:pk>/', views.DepartmentUpdateView.as_view(), name='update'),
    path('department-detail/<int:pk>/', views.DepartmentDetailView.as_view(), name='detail'),
    path('department-delete/<int:pk>/', views.DepartmentDeleteView.as_view(), name='delete'),
]