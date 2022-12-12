from django.contrib import admin

from .models import Mathgame

@admin.register(Mathgame)
class MathgameAdmin(admin.ModelAdmin):
    model = Mathgame
    list_display = ['score', 'max_number', 'operation', 'end_time']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('score', 'max_number', 'operation', 'end_time')

        return ()