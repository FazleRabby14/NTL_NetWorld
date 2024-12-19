from django.shortcuts import render
from django.core.mail import send_mail
from .models import contactInfo

def indexpage(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        # Save the data to the database
        contact_info = contactInfo(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, message=message)
        contact_info.save()

        # Prepare email message
        email_message = f"First name: {first_name}\nLast name: {last_name}\nEmail: {email}\nPhone number: {phone_number}\nMessage: {message}"

        # Send email
        send_mail(
            'New Contact Enquiry',
            email_message,
            'sw-fazla.rabby@networld-bd.com',
            ['info@networld-bd.com'],
            fail_silently=False,
        )

        # Return the page with a success message
        return render(request, 'index.html', {'success': True})

    return render(request, 'index.html')

def Ncr21(request):
    
    return render(request, 'ncr21.html')

def Ncr27(request):
    
    return render(request, 'ncr27.html')

def Ncr61(request):
    
    return render(request, 'ncr61.html')

def Ncr64(request):
    
    return render(request, 'ncr64.html')

def NcrSE(request):
    
    return render(request, 'ncrSE.html')

