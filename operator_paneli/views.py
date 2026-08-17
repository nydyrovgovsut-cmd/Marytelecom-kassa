from django.shortcuts import render
from billing.models import Ticket

def operator_panel(request, counter_id):
    play_sound = False
    
    if request.method == 'POST':
        if request.POST.get('action') == 'next':
            next_ticket = Ticket.objects.filter(service_type='Balans doldurmak', status='waiting').order_by('created_at').first()
            if next_ticket:
                next_ticket.status = 'calling'
                next_ticket.cash_desk = counter_id
                next_ticket.save()
                play_sound = True

    current_ticket = Ticket.objects.filter(
        service_type='Balans doldurmak', 
        cash_desk=counter_id, 
        status='calling'
    ).order_by('-created_at').first()

    waiting_ahead = Ticket.objects.filter(service_type='Balans doldurmak', status='waiting').count()

    context = {
        'counter_id': counter_id,
        'ticket': current_ticket,
        'waiting_ahead': waiting_ahead,
        'play_sound': play_sound,
    }
    return render(request, 'operator_panel.html', context)

def operator_panel_internet(request, counter_id):
    play_sound = False
    
    if request.method == 'POST':
        if request.POST.get('action') == 'next':
            next_ticket = Ticket.objects.filter(service_type='Internet', status='waiting').order_by('created_at').first()
            if next_ticket:
                next_ticket.status = 'calling'
                next_ticket.cash_desk = counter_id
                next_ticket.save()
                play_sound = True
    current_ticket = Ticket.objects.filter(
        service_type='Internet', 
        cash_desk=counter_id, 
        status='calling'
    ).order_by('-created_at').first()

    waiting_ahead = Ticket.objects.filter(service_type='Internet', status='waiting').count()

    context = {
        'counter_id': counter_id,
        'ticket': current_ticket,
        'waiting_ahead': waiting_ahead,
        'play_sound': play_sound,
    }
    return render(request, 'operator_paneli_Internet.html', context)

def operator_panel_pochta(request, counter_id):
    play_sound = False
    
    if request.method == 'POST':
        if request.POST.get('action') == 'next':
            next_ticket = Ticket.objects.filter(service_type='Matty ýükleri ugratmak üçin', status='waiting').order_by('created_at').first()
            if next_ticket:
                next_ticket.status = 'calling'
                next_ticket.cash_desk = counter_id
                next_ticket.save()
                play_sound = True

    current_ticket = Ticket.objects.filter(
        service_type='Matty ýükleri ugratmak üçin', 
        cash_desk=counter_id, 
        status='calling'
    ).order_by('-created_at').first()

    waiting_ahead = Ticket.objects.filter(service_type='Matty ýükleri ugratmak üçin', status='waiting').count()

    context = {
        'counter_id': counter_id,
        'ticket': current_ticket,
        'waiting_ahead': waiting_ahead,
        'play_sound': play_sound,
    }
    return render(request, 'operator_paneli_poçta.html', context)
