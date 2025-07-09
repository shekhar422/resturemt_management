from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime


from .models import Contact, booking, veg_item, non_veg_item, Dessert, Cold_Drink

def index(request):
    menus = {
        'veg': veg_item.objects.all(),
        'nonveg': non_veg_item.objects.all(),
        'dessert': Dessert.objects.all(),
        'colddrink': Cold_Drink.objects.all(),
    }
    context = {'menus': menus}
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        massage = request.POST.get("massage")  # typo 'massage' kept as in model

        new_contact = Contact(
            name=name,
            phone_number=phone_number,
            email=email,
            massage=massage,
            date=datetime.today()
        )
        new_contact.save()
        messages.success(request, "Contact message sent successfully!")
    return render(request, "contact.html")

def book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        persons = request.POST.get('persons')
        booking_date = request.POST.get('booking_date')

        new_booking = booking(
            name=name,
            phone_number=phone_number,
            persons=persons,
            booking_date=booking_date
        )
        new_booking.save()
        messages.success(request, "Booking successful!")
    return render(request, "book.html")

