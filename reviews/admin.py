from django.contrib import admin

from .models import Review

@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['first_name', 'last_name', 'email', 'comment', 'created']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created')

        return ()