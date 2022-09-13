from django.urls import path

from car import views

urlpatterns = [
    path('create-car/', views.CarCreateView.as_view(), name='create_car'),
    path('list-of-cars/', views.CarListView.as_view(), name='list_of_cars'),
    path('update-car/<int:pk>/', views.CarUpdateView.as_view(), name='update_car'),
    path('delete-car/<int:pk>/', views.CarDeleteView.as_view(), name='delete_car'),
    path('detail-car/<int:pk>/', views.CarDetailView.as_view(), name='detail_car'),
]
