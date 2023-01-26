from django.contrib import admin

from .models import Mathgame, MathgameScore

@admin.register(Mathgame)
class MathgameAdmin(admin.ModelAdmin):
    model = Mathgame
    list_display = ['score', 'operation', 'max_number', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('updated')

        return ()

@admin.register(MathgameScore)
class MathgameScoreAdmin(admin.ModelAdmin):
    model = MathgameScore
    list_display = ['mathgame', 'user', 'scores']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('created', 'updated')
        return ()