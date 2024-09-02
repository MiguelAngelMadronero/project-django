from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ContactForm
from .models import Contact
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, "home.html")

def home_contact(request):
    return render(request, "home_contact.html")

def signup(request):
    if request.method == 'GET':
         return render(request, "signup.html", {
            "form": UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            #register user
            try:
                user=User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("contacts")
            except IntegrityError:
                return render(request, "signup.html",{
                    "form": UserCreationForm,
                    "error":"Username already exists"
                })
        
        return render(request, "signup.html",{
                    "form": UserCreationForm,
                    "error":"Passwords do not match"
        })

@login_required    
def contacts(request):
    contact_title="Contactos Agregados"
    contacts = Contact.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, "contacts.html", {
        "contacts": contacts,
        "contact_title": contact_title
    })

@login_required
def contacts_completed(request):
    contact_title= "Contactos Favoritos"
    contacts=Contact.objects.filter(user=request.user, datecompleted__isnull=False).order_by
    ("-datecompleted")
    return render(request, "contacts.html",{
        "contacts":contacts,
        "contact_title": contact_title
    })

@login_required
def create_contact(request):
    if request.method == "GET":
        return render(request, "create_contact.html", {
            "form": ContactForm
        })
    else:
        try:
            form=ContactForm(request.POST)
            new_contact=form.save(commit=False)
            new_contact.user= request.user
            new_contact.save()
            print(new_contact)
            return redirect("contacts")
        except ValueError:
            return render(request, "create_contact.html", {
                "form": ContactForm,
                "error": "Please provide valide data"
            })

@login_required
def contact_detail(request, contact_id):
    if request.method == "GET":
        contact=get_object_or_404(Contact, pk=contact_id, user=request.user)
        form=ContactForm(instance=contact)
        return render(request, "contact_detail.html",{
            "contact":contact,
            "form": form
        })
    else:
        try:
            contact=get_object_or_404(Contact, pk=contact_id, user=request.user)
            form=ContactForm(request.POST, instance=contact)
            form.save()
            return redirect("contacts")
        except ValueError:
            return render(request, "contact_detail.html",{
                "contact":contact,
                "form": form,
                "error": "Error updating contact"
            })

@login_required           
def complete_contact(request, contact_id):
    contact=get_object_or_404(Contact, pk=contact_id, user=request.user)
    if request.method == "POST":
        contact.datecompleted =  timezone.now()
        contact.save()
        return redirect("contacts")

@login_required
def delete_contact(request, contact_id):
    contact=get_object_or_404(Contact, pk=contact_id, user=request.user)
    if request.method == "POST":
        contact.delete()
        return redirect("contacts")  

@login_required
def signout(request):
    logout(request)
    return redirect("home_contact")

def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {
            "form": AuthenticationForm
        })
    else:
        user=authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(request.POST)
        if user is None:
            return render(request, "signin.html", {
                "form": AuthenticationForm,
                "error": "Username or password is incorrect"
            })
        else:
            login(request, user)
            return redirect("contacts")



        




    
   