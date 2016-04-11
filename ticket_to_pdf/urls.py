from django.conf.urls import url, include
from django.contrib import admin

from common.views import IndexRedirectView
from tickets.urls import ticket_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^accounts/', accounts_urls),
    url(r'^$', IndexRedirectView.as_view()),
    url(r'^tickets/', include(ticket_patterns, namespace='tickets')),
]
