from django.urls import path

from roadTax import views

urlpatterns = [
    path('create-roadTax/', views.RoadTaxCreateView.as_view(), name='create_roadTax'),
    path('list-of-roadTaxes/', views.RoadTaxListView.as_view(), name='list_of_roadTaxes'),
    path('update-roadTax/<int:pk>/', views.RoadTaxUpdateView.as_view(), name='update_roadTax'),
    path('delete-roadTax/<int:pk>/', views.RoadTaxDeleteView.as_view(), name='delete_roadTax'),

]
