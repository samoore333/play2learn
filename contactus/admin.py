from django.contrib import admin

from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    list_display = ['first_name', 'last_name', 'email', 'subject', 'message', 'created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created')

        return ()