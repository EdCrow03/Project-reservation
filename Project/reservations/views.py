# reservations/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reservation
from authentification.models import Utilisateur
from .forms import ReservationForm
from django.urls import reverse
# Create your views here.
#def reservations(request):
#    return render(request, 'reservations/index.html')

def index(request):
    # Logique supplémentaire si nécessaire
    return render(request, 'index.html')

def create_reservation(request):
    if request.method == 'POST':
        table_type = request.POST.get('type-table')
        reservation_date = request.POST.get('date')
        number_of_guests = request.POST.get('number-guests')
        reservation_time = request.POST.get('time')
        message = request.POST.get('message')
        
        user_email = request.session.get('user_email')
        if user_email:
            utilisateur = Utilisateur.objects.get(email=user_email)

            reservation = Reservation(
                utilisateur=utilisateur,
                table_type=table_type,
                reservation_date=reservation_date,
                number_of_guests=number_of_guests,
                reservation_time=reservation_time,
                message=message
            )
            reservation.save()
        return redirect('/reservations/')  # Redirigez vers une page de succès ou autre
        
    return render(request, '/reservations/')


def user_reservations(request):
    print("test fct")
    user_email = request.session.get('user_email')
    if user_email:
        utilisateur = Utilisateur.objects.get(email=user_email)
        reservations = Reservation.objects.filter(utilisateur=utilisateur)
        print("test user")
        return render(request, 'reservations/index.html', {'reservations': reservations})
    else:
        return redirect('/reservation')  # Redirige vers la page de connexion si l'email n'est pas trouvé dans la session

def editreservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.method == 'POST':
        # Traitement du formulaire de modification ici
        reservation.table_type = request.POST.get('table_type')
        reservation.reservation_date = request.POST.get('reservation_date')
        reservation.number_of_guests = int(request.POST.get('number_of_guests'))
        reservation.reservation_time = request.POST.get('reservation_time')
        reservation.message = request.POST.get('message')
        reservation.save()
        return redirect('/reservations/user_reservation/')  # Redirection après modification
    
    context = {
        'reservation': reservation,
    }
    return render(request, 'reservations/edit_reservation/index.html', context)

def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    if request.method == 'POST':
        reservation.delete()
        return redirect('/reservations/user_reservation/')  # Rediriger vers la liste des réservations après la suppression
    return render(request, 'reservations/index.html', {'reservation': reservation})

def controlpanel(request):
        reservations = Reservation.objects.all()
        return render(request, 'controlpanel/index.html', {'reservations': reservations})