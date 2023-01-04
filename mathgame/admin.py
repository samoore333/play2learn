from django.contrib import admin

from .models import Mathgame, Gameplay

@admin.register(Mathgame)
class MathgameAdmin(admin.ModelAdmin):
    model = Mathgame
    list_display = ['operation', 'max_number']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('operation', 'max_number', 'slug')

        return ()

@admin.register(Gameplay)
class GameplayAdmin(admin.ModelAdmin):
    model = Gameplay
    list_display = ['mathgame', 'user', 'correct_answer', 'incorrect_answer', 'score']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created', 'updated')
        return ()