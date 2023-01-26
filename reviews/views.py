import html
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from common.utils.email import send_email
from .models import Review
from .forms import ReviewsForm

class ReviewsAppView(CreateView):
    model = Review
    form_class = ReviewsForm
    success_url = reverse_lazy('reviews:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'samoore333@gmail.com'
        subject = 'Review Form'
        content = f'''<p>Hey Admin:</p>
            <p>Review received and needs your approval:
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)

class ReviewsAppThanksView(TemplateView):
    template_name = 'reviews/thanks.html'