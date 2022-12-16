from django.contrib import admin

from .models import Reviews

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    model = Reviews
    list_display = ['first_name', 'last_name', 'email', 'comment']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('first_name', 'last_name', 'email', 'comment')

        return ()