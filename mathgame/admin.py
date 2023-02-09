from django.contrib import admin

from common.admin import Play2LearnAdmin

from .models import Mathgame, MathgameScore

@admin.register(Mathgame)
class MathgameAdmin(Play2LearnAdmin):
    model = Mathgame
    list_display = ['operation', 'max_number', 'score', 'updated', 'user']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('updated',)

        return ()

@admin.register(MathgameScore)
class MathgameScoreAdmin(Play2LearnAdmin):
    model = MathgameScore
    list_display = ['mathgame', 'user', 'scores']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('created', 'updated')
        return ()