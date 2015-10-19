from django.contrib import admin
from pyconfr.simplepoll.models import Poll


class PollAdmin(admin.ModelAdmin):
    search_fields = ('user__first_name',)
    list_display = ('get_user_name', 'phone', 'willbepresentsaturday', 'willbetheresunday', 'goodies', 'tshirtsize', 'diner', 'iarriveby', 'arrivaldate', 'arrivalhour', 'iwillgoby', 'dateofdeparture', 'hourofdeparture' )

    def get_user_name(self, obj):
        if obj.user:
            return obj.user.first_name +' '+ obj.user.last_name
        else:
            return None

admin.site.register(Poll, PollAdmin)

