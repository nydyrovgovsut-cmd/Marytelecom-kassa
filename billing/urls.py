from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    # Balans hyzmaty üçin ýollar
    path('', views.index, name='index'),
    path('ticket/balans/create/', views.Balans_doldurmak, name='Balans_ticket'),
    path('ticket/balans/print/<int:ticket_id>/', views.print_ticket, name='print_ticket'),

    # Internet hyzmaty üçin ýollar
    path('ticket/internet/create/', views.Internet_hyzmatlary, name='Internet'),
    path('ticket/internet/print1/<int:ticket_id>/', views.Internet1, name='Internet1'),

    # Telefon/IPTV hyzmaty üçin ýollar
    path('ticket/telefon_iptv/create/', views.Telefon_IPTV, name='Telefon/IPTV'),
    path('ticket/telefon_iptv/print2/<int:ticket_id>/', views.Telefon_IPTV2, name='Telefon_IPTV2'),

    # Maslahat hyzmaty üçin ýollar
    path('ticket/maslahat/create/', views.Maslahat, name='Maslahat'),
    path('ticket/maslahat/print4/<int:ticket_id>/', views.Maslahat4, name='Maslahat3'),

    # Talonlary çykarmak üçin ýollar
    path('ticket/balans/print/<int:ticket_id>/', views.print_ticket, name='print_ticket'),
    path('ticket/internet/print1/<int:ticket_id>/', views.Internet1, name='Internet1'),
    path('ticket/telefon_iptv/print2/<int:ticket_id>/', views.Telefon_IPTV2, name='Telefon_IPTV2'),
    path('ticket/maslahat/print4/<int:ticket_id>/', views.Maslahat4, name='Maslahat4'),

]

