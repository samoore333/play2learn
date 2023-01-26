from django.contrib import admin

from common.admin import Play2LearnAdmin

from .models import Review

@admin.register(Review)
class ReviewsAdmin(Play2LearnAdmin):
    model = Review
    list_display = ['first_name', 'last_name', 'email', 'comment', 'approved']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('created',)

        return ()