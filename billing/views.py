from django.shortcuts import get_object_or_404, redirect, render
from .models import Ticket

def index(request):
     return render(request, 'index.html')

from django.utils import timezone

def Balans_doldurmak(request):
    """Balans doldurmak üçin talon döretmek funksiýasy"""
    if request.method == 'POST':
        service_type = 'Balans doldurmak'
        prefix = 'B'
        cash_desk = '1'

        today = timezone.localdate()


        last_ticket = Ticket.objects.filter(service_type=service_type).order_by('-id').first()
        

        if last_ticket and last_ticket.created_at.date() == today and '-' in str(last_ticket.ticket_number):
            try:
                last_number = int(str(last_ticket.ticket_number).split('-')[1])
                next_number = last_number + 1
            except (ValueError, IndexError):
                next_number = 1
        else:
            next_number = 1


        ticket_number = f"{prefix}-{next_number:03d}"
        
        ticket = Ticket.objects.create(
            ticket_number=ticket_number,
            service_type=service_type,
            cash_desk=cash_desk,
            status='waiting'
        )

        return redirect('print_ticket', ticket_id=ticket.id)

    return render(request, 'user-form.html')

def Internet_hyzmatlary(request):
    """Internet hyzmatlary üçin talon döretmek funksiýasy"""
    if request.method == 'POST':
        service_type = 'Internet hyzmatlary'
        prefix = 'I'
        cash_desk = '4,5,6'

        today = timezone.localdate()

   
        last_ticket = Ticket.objects.filter(service_type=service_type).order_by('-id').first()
        
        if last_ticket and last_ticket.created_at.date() == today and '-' in str(last_ticket.ticket_number):
            try:
                last_number = int(str(last_ticket.ticket_number).split('-')[1])
                next_number = last_number + 1
            except (ValueError, IndexError):
                next_number = 1
        else:
    
            next_number = 1

        ticket_number = f"{prefix}-{next_number:03d}"
        
        ticket = Ticket.objects.create(
            ticket_number=ticket_number,
            service_type=service_type,
            cash_desk=cash_desk,
            status='waiting'
        )

        return redirect('Internet1', ticket_id=ticket.id)

    return render(request, 'user-form1.html')



def Telefon_IPTV(request):
    """Telefon/IPTV doldurmak üçin talon döretmek funksiýasy"""
    if request.method == 'POST':
        service_type = 'Telefon/IPTV'
        prefix = 'T'
        cash_desk = '3'

        # Получаем сегодняшнюю дату
        today = timezone.localdate()

        last_ticket = Ticket.objects.filter(service_type=service_type).order_by('-id').first()
        
        if last_ticket and last_ticket.created_at.date() == today and '-' in str(last_ticket.ticket_number):
            try:
                last_number = int(str(last_ticket.ticket_number).split('-')[1])
                next_number = last_number + 1
            except (ValueError, IndexError):
                next_number = 1
        else:
            next_number = 1


        ticket_number = f"{prefix}-{next_number:03d}"
        
        ticket = Ticket.objects.create(
            ticket_number=ticket_number,
            service_type=service_type,
            cash_desk=cash_desk,
            status='waiting'
        )

        return redirect('Telefon_IPTV2', ticket_id=ticket.id)

    return render(request, 'user-form2.html')



def telegraf_create_view(request):
    """Telegraf doldurmak üçin talon döretmek funksiýasy (POST gelende ýasaýar)"""
    if request.method == 'POST':
        service_type = 'Haty almak we ugratmak'
        prefix = 'H'
        cash_desk = '15'

    
        today = timezone.localdate()


        last_ticket = Ticket.objects.filter(service_type=service_type).order_by('-id').first()
        
     
        if last_ticket and last_ticket.created_at.date() == today and '-' in str(last_ticket.ticket_number):
            try:
                last_number = int(str(last_ticket.ticket_number).split('-')[1])
                next_number = last_number + 1
            except (ValueError, IndexError):
                next_number = 1
        else:

            next_number = 1

   
        ticket_number = f"{prefix}-{next_number:03d}"
        
        ticket = Ticket.objects.create(
            ticket_number=ticket_number,
            service_type=service_type,
            cash_desk=cash_desk,
            status='waiting'
        )

        return redirect('Telegraf4', ticket_id=ticket.id)

    return render(request, 'user-form3.html')

from django.utils import timezone

def Poçta_hyzmatlary(request):
    """Poçta hyzmatlary üçin talon döretmek funksiýasy"""
    if request.method == 'POST':
        service_type = 'Poçta hyzmatlary'
        prefix = 'P'
        cash_desk = '11,12,13'

 
        today = timezone.localdate()

       
        last_ticket = Ticket.objects.filter(service_type=service_type).order_by('-id').first()
        

        if last_ticket and last_ticket.created_at.date() == today and '-' in str(last_ticket.ticket_number):
            try:
                last_number = int(str(last_ticket.ticket_number).split('-')[1])
                next_number = last_number + 1
            except (ValueError, IndexError):
                next_number = 1
        else:
          
            next_number = 1


        ticket_number = f"{prefix}-{next_number:03d}"
        
        ticket = Ticket.objects.create(
            ticket_number=ticket_number,
            service_type=service_type,
            cash_desk=cash_desk,
            status='waiting'
        )

        return redirect('Poçta5', ticket_id=ticket.id)

    return render(request, 'user-form4.html')

from django.utils import timezone

def print_ticket(request, ticket_id):
    """Balans talonyny çap etmek we görkezmek"""
    ticket = get_object_or_404(Ticket, id=ticket_id)

    ticket_date = ticket.created_at.date()


    waiting_ahead = Ticket.objects.filter(
        service_type=ticket.service_type, 
        status='waiting',
        created_at__date=ticket_date,  
        id__lt=ticket.id               
    ).count()

    context = {
        'ticket': ticket,
        'waiting_ahead': waiting_ahead,
    }
    return render(request, 'KassaN1.html', context)

def Internet1(request, ticket_id):
    """Internet talonyny çap etmek we görkezmek"""
    ticket = get_object_or_404(Ticket, id=ticket_id)

    ticket_date = ticket.created_at.date()

    waiting_ahead = Ticket.objects.filter(
        service_type=ticket.service_type, 
        status='waiting', 
        created_at__date=ticket_date,
        id__lt=ticket.id
    ).count()

    context1 = {
        'ticket': ticket,
        'waiting_ahead': waiting_ahead,
    }
    return render(request, 'Internet_hyzmaty.html', context1)

def Telefon_IPTV2(request, ticket_id):
    """Telefon/IPTV talonyny çap etmek we görkezmek"""
    ticket = get_object_or_404(Ticket, id=ticket_id)

    ticket_date = ticket.created_at.date()

    waiting_ahead = Ticket.objects.filter(
        service_type=ticket.service_type, 
        status='waiting', 
        created_at__date=ticket_date,
        id__lt=ticket.id
    ).count()

    context2 = {
        'ticket': ticket,
        'waiting_ahead': waiting_ahead,
    }
    return render(request, 'Telefon_IPTV.html', context2)

def Telegraf(request, ticket_id=None):
    """Döredilen telegraf talonyny çap etmek we görkezmek"""
    ticket = get_object_or_404(Ticket, id=ticket_id)

    ticket_date = ticket.created_at.date()

    waiting_ahead = Ticket.objects.filter(
        service_type=ticket.service_type, 
        status='waiting', 
        created_at__date=ticket_date,
        id__lt=ticket.id
    ).count()

    context3 = {
        'ticket': ticket,
        'waiting_ahead': waiting_ahead,
    }
    return render(request, 'Telegraf.html', context3)

