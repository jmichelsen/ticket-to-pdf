import pdfkit

from django.views.generic import DetailView, CreateView, ListView
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponse
from django.conf import settings

from tickets.forms import TicketForm
from tickets.models import Ticket, Buyer, Seller


class BuyerCreateView(CreateView):
    template_name = 'create_buyer.html'
    success_url = reverse_lazy('tickets:list')
    model = Buyer
    fields = '__all__'


class SellerCreateView(CreateView):
    template_name = 'create_seller.html'
    success_url = reverse_lazy('tickets:list')
    model = Seller
    fields = '__all__'


class TicketListView(ListView):
    template_name = 'tickets_list.html'
    model = Ticket


class TicketCreateView(CreateView):
    template_name = 'create_ticket.html'
    form_class = TicketForm
    success_url = reverse_lazy('tickets:list')


class TicketDetailView(DetailView):
    template_name = 'ticket_detail.html'
    model = Ticket


class PDFDetailView(TicketDetailView):
    def get(self, request, *args, **kwargs):
        ticket_url = reverse('tickets:detail',
                             kwargs=kwargs)
        full_ticket_url = '{}{}'.format(settings.HOSTNAME, ticket_url)
        pdfkit.from_url(full_ticket_url, 'ticket.pdf')
        with open('ticket.pdf', 'r') as pdf:
            response = HttpResponse(pdf.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline;filename=ticket.pdf'
            return response
