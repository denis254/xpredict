from django.contrib import admin

from . models import FreeTipsGames,SingleBetGames,VipTips, PunterPick, RollOver, Notification, Jackpot

admin.site.register(FreeTipsGames)

admin.site.register(SingleBetGames)

admin.site.register(VipTips)

admin.site.register(PunterPick)

admin.site.register(RollOver)

admin.site.register(Notification)

admin.site.register(Jackpot)
