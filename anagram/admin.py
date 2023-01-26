from django.contrib import admin

from common.admin import Play2LearnAdmin

from .models import Anagramgame

@admin.register(Anagramgame)
class AnagramAdmin(Play2LearnAdmin):
    model = Anagramgame
    list_display = ['score', 'word_length', 'end_time']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('end_time',)

        return ()