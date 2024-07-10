from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Utilisateur
import datetime
# Create your views here.

def home(request):
    return render(request, 'index.html')

def auth(request):
    return render(request, 'authentification/login/index.html')

def login(request):
    print('1')
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print('2')
        try:
            utilisateur = Utilisateur.objects.get(email=email)
            if utilisateur.verify_password(password):
                # Authentification réussie
                print('3')
                request.session['user_email'] = email
                request.session['connected'] = True
                request.session['is_staff'] = utilisateur.is_staff
                request.session['nom_et_prenom'] = utilisateur.nom_et_prenom
                return redirect('home')  # Rediriger vers la page d'accueil après le login
            else:
                print('4')
                messages.error(request, "Email ou mot de passe incorrect.")
        except Utilisateur.DoesNotExist:
            print('5')
            messages.error(request, "Email ou mot de passe incorrect.")
    print('6')
    return render(request, 'authentification/login/index.html')

def signup(request):
    print('Requête reçue:', request.method)
    print('1')
    if request.method == 'POST':
        # Récupération des données du formulaire
        nom_et_prenom = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        date_naissance = request.POST.get('date')
        numero_telephone = request.POST.get('phone')
        print('2')
        # Validation des mots de passe
        if password1 != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return render(request, 'authentification/signup/index.html', {
                'username': nom_et_prenom,
                'email': email,
                'date': date_naissance,
                'phone': numero_telephone,
            })
        
        # Validation de la date de naissance
        try:
            date_naissance = datetime.datetime.strptime(date_naissance, '%Y-%m-%d').date()
            print('4')
        except ValueError:
            messages.error(request, "Entrez une date de naissance valide.")
            return render(request, 'authentification/signup/index.html', {
                'username': nom_et_prenom,
                'email': email,
                'date': date_naissance,
                'phone': numero_telephone,
            })

        if Utilisateur.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return render(request, 'authentification/signup/index.html', {
                'username': nom_et_prenom,
                'date': date_naissance,
                'phone': numero_telephone,
        })

        
        # Création de l'utilisateur
        is_staff = False  # Pour que is_staff soit toujours False lors de la création
        utilisateur = Utilisateur.objects.create(
            nom_et_prenom=nom_et_prenom,
            email=email,
            password=password1,
            date_naissance=date_naissance,
            numero_telephone=numero_telephone,
            is_staff=is_staff
        )
        
        # Redirection ou traitement supplémentaire après création de l'utilisateur
        print('6')
        utilisateur.save()
        return redirect('/authentification/login')
        print('7')  # Redirige vers la page d'accueil après création
    print('8')
    return render(request, 'authentification/signup/index.html')
    print('9')  # Rendre le template du formulaire


def logout_view(request):
    request.session.flush()
    return redirect('home')

