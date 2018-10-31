from django.contrib import admin

from . models import FreeTipsGames, VipTips, PunterPick, RollOver

from import_export.admin import ImportExportModelAdmin

from django.contrib.auth.models import User

from django.contrib.auth.admin import UserAdmin as BaseAdmin

from import_export import resources

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = UserResource

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(FreeTipsGames)
class FreeTipsGamesAdmin(ImportExportModelAdmin):
    pass

@admin.register(VipTips)
class VipTipsAdmin(ImportExportModelAdmin):
    pass

@admin.register(PunterPick)
class PunterPickAdmin(ImportExportModelAdmin):
    pass

@admin.register(RollOver)
class RollOverAdmin(ImportExportModelAdmin):
    pass
