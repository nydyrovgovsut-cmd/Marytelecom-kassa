from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [

    # TMCELL üçin operator_paneli
    path('operator/balans/<int:counter_id>/', views.operator_panel, name='operator_panel'),
    # Internet hyzmaty üçin operator_paneli
    path('operator5/internet/<str:counter_id>/', views.operator_panel_internet, name='operator_internet'),
    # Aragatnaşyk hyzmaty üçin operator_paneli
    path('operator2/aragatnaşyk/<str:counter_id>/', views.operator_paneli_aragatnaşyk, name='operator_panel_Aragatnaşyk'),
    # Telegraf hyzmaty üçin operator_paneli
    path('operator3/telegraf/<str:counter_id>/', views.operator_paneli_telegraf, name='operator_panel_Telegraf'),
    # Poçta üçin operator paneli
    path('operator4/pochta/<str:counter_id>/', views.operator_panel_pochta, name='operator_panel_poсhta'),
    # Router sazlamak üçin operator_paneli
    path('operator6/Router/', views.operator_panel_Router, name='operator_panel_Router'),
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

    # Telegraf hyzmaty üçin ýollar
    path('ticket/telegraf/create/', views.telegraf_create_view, name='Telegraf'),
    path('ticket/telegraf/<int:ticket_id>/', views.Telegraf, name='Telegraf4'),

    # Poçta hyzmaty üçin ýollar
    path('ticket/Poçta/create/', views.Poçta_hyzmatlary, name='Poçta'),
    path('ticket/Poçta/<int:ticket_id>/', views.Poçta5, name='Poçta5'),

     # Routeri sazlamak üçin ýollar
    path('ticket/Router/create/', views.Router_sazlamak, name='Router'),
    path('ticket/Router/print7/<int:ticket_id>/', views.Router5, name='Router6'),

    # Talonlary çykarmak üçin ýollar
    path('ticket/balans/print/<int:ticket_id>/', views.print_ticket, name='print_ticket'),
    path('ticket/internet/print1/<int:ticket_id>/', views.Internet1, name='Internet1'),
    path('ticket/telefon_iptv/print2/<int:ticket_id>/', views.Telefon_IPTV2, name='Telefon_IPTV2'),
    path('ticket/telegraf/<int:ticket_id>/', views.Telegraf, name='Telegraf4'),
    path('ticket/Poçta/<int:ticket_id>/', views.Poçta5, name='Poçta5'),
    path('ticket/Router/print7/<int:ticket_id>/', views.Router5, name='Router6'),


]
