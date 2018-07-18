from django.conf.urls import url
from django.views.generic import ListView
from prosite.models import Block,Album, Text
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url (r'^$', views.main_page, name='main_page'),
    url (r'^main_page/$', views.main_page, name='main_page'),
    url (r'^rsvp/$', views.rsvp, name='rsvp'),
    url (r'^event/$', views.event, name='event'),
    url (r'^photo/$', views.photo, name='photo'),

    url (r'^party/$', views.party, name='party'),
    url (r'^travel/$', views.travel, name='travel'),
    url (r'^gift/$', views.gift, name='gift'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

