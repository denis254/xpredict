from django.urls import path, include

from palsbet import views

from . views import rolloverh, play, information, register, punterpick, homeviptips, payment, homevip, timeofsending, modeofsending, home, viewolderesults, androidapp, rollover, viptips, guide, howmanyodds, privacy

urlpatterns = [

    path('', home),

    path('play/', play),

    path('privacy/', privacy),

    path('home/', home),

    path('information/', information),

    path('register/', register),

    path('crafttechsolution/', views.optout, name = "optout"),

    path('viewolderesults/', viewolderesults),

    path('androidapp/', androidapp),

    path('rollover/', rollover),

    path('viptips/', viptips),

    path('guide/', guide),

    path('howmanyodds/', howmanyodds),

    path('modeofsending/', modeofsending),

    path('timeofsending/', timeofsending),

    path('accounts/', include('django.contrib.auth.urls')),

    path('home_vip/', homevip),

    path('payment/', payment),

    path('homevip/', homevip),

    path('homeviptips/', homeviptips),

    path('homepunterpicks/', punterpick),

    path('homerollover/', rolloverh),
]
