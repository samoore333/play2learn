from django.contrib import admin

from .models import Anagramgame

@admin.register(Anagramgame)
class AnagramAdmin(admin.ModelAdmin):
    model = Anagramgame
    list_display = ['score', 'max_number', 'operation', 'end_time']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('score', 'max_number', 'operation', 'end_time')

        return ()