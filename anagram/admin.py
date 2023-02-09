from django.contrib import admin

from common.admin import Play2LearnAdmin

from .models import Anagramgame

@admin.register(Anagramgame)
class AnagramgameAdmin(Play2LearnAdmin):
    model = Anagramgame
    list_display = ['word_length', 'score', 'updated', 'user']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('updated',)

        return ()