from django.urls import path

from mot import views

urlpatterns = [
    path('create-mot/', views.MotCreateView.as_view(), name='create_mot'),
    path('list-of-mots/', views.MotListView.as_view(), name='list_of_mots'),
    path('update-mot/<int:pk>/', views.MotUpdateView.as_view(), name='update_mot'),
    path('delete-mot/<int:pk>/', views.MotDeleteView.as_view(), name='delete_mot'),

]
