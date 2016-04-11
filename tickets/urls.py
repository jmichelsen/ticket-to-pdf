from django.conf.urls import url

from tickets import views as ticket_views

ticket_patterns = [
    url(r'^$', ticket_views.TicketListView.as_view(), name='list'),
    url(r'^create/$', ticket_views.TicketCreateView.as_view(),
        name='create_ticket'),
    url(r'^(?P<pk>[\w]+)/$', ticket_views.TicketDetailView.as_view(),
        name='detail'),
    url(r'^pdf/(?P<pk>[\w]+)/$', ticket_views.PDFDetailView.as_view(),
        name='pdf_detail'),

    url(r'^create-buyer/$', ticket_views.BuyerCreateView.as_view(),
        name='create_buyer'),
    url(r'^create-seller/$', ticket_views.SellerCreateView.as_view(),
        name='create_seller'),


]
