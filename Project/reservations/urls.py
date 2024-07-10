from django.urls import path
from . import views

app_name = 'reservations'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_reservation/', views.create_reservation, name='create_reservation'),
    path('user_reservation/', views.user_reservations, name='user_reservations'),
    path('edit_reservation/<int:reservation_id>/', views.editreservation, name='edit_reservation'),
    path('delete_reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('controlpanel/', views.controlpanel, name='controlpanel'),
]