from django.contrib import admin

from .models import Anagram

@admin.register(Anagram)
class AnagramAdmin(admin.ModelAdmin):
    model = Anagram
    list_display = ['score', 'max_number', 'operation', 'end_time']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('score', 'max_number', 'operation', 'end_time')

        return ()