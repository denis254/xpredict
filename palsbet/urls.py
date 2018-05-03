from django.urls import path, include

from palsbet import views

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'FreeTipsGames', views.FreeTipsGamesViewSet)

router.register(r'SingleBetGames', views.SingleBetGamesViewSet)

from . views import rolloverh, punterpick, homeviptips, payment, homevip, timeofsending, modeofsending, home, viewolderesults, singlebet, androidapp, jackpot, rollover, viptips, guide, howmanyodds

urlpatterns = [

    path('freetipsp/', include(router.urls)),

    path('', home),

    path('home/', home),

    path('viewolderesults/', viewolderesults),

    path('singlebet/', singlebet),

    path('androidapp/', androidapp),

    path('jackpot/', jackpot),

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
