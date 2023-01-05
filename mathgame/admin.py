from django.contrib import admin

from .models import Mathgame

@admin.register(Mathgame)
class MathgameAdmin(admin.ModelAdmin):
    model = Mathgame
    list_display = ['operation', 'max_number']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('operation', 'max_number', 'slug', 'score', 'updated')

        return ()