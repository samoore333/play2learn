from django.contrib import admin

from .models import Mathgame, MathgameScore

@admin.register(Mathgame)
class MathgameAdmin(admin.ModelAdmin):
    model = Mathgame
    list_display = ['operation', 'max_number', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('operation', 'max_number', 'slug', 'updated')

        return ()

@admin.register(MathgameScore)
class MathgameScoreAdmin(admin.ModelAdmin):
    model = MathgameScore
    list_display = ['mathgame', 'user', 'score']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('created', 'updated')
        return ()