from django.contrib import admin

from common.admin import Play2LearnAdmin

from .models import Contact

@admin.register(Contact)
class ContactAdmin(Play2LearnAdmin):
    model = Contact
    list_display = ['first_name', 'last_name', 'email', 'subject', 'message']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created',)

        return ()