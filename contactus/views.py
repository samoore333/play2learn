import html
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from common.utils.email import send_email
from .models import Contact
from .forms import ContactUsForm

class ContactUsAppView(CreateView):
    model = Contact
    form_class = ContactUsForm
    success_url = reverse_lazy('contactus:thanks')

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'samoore333@gmail.com'
        subject = 'Contact Us Form'
        content = f'''<p>Contact Us message received:</p>
            <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        
        content += '</ol>'

        send_email(to, subject, content)
        return super().form_valid(form)

class ContactUsThanksView(TemplateView):
    template_name = 'contactus/thanks.html'