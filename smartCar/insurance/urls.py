from django.urls import path

from insurance import views

urlpatterns = [
    path('create-insurance/', views.InsuranceCreateView.as_view(), name='create_insurance'),
    path('list-of-insurances/', views.InsuranceListView.as_view(), name='list_of_insurances'),
    path('update-insurance/<int:pk>/', views.InsuranceUpdateView.as_view(), name='update_insurance'),
    path('delete-insurance/<int:pk>/', views.InsuranceDeleteView.as_view(), name='delete_insurance'),
]
