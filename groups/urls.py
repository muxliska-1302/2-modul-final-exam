from django.urls import path
from . import views


app_name = 'groups'

urlpatterns = [
    path('groups-list/', views.GroupListView.as_view(), name='list'),
    path('group-create/', views.GroupCreateView.as_view(), name='create'),
    path('group-update/<int:pk>/', views.GroupUpdateView.as_view(), name='update'),
    path('group-detail/<int:pk>/', views.GroupDetailView.as_view(), name='detail'),
    path('group-delete/<int:pk>/', views.GroupDeleteView.as_view(), name='delete'),
]