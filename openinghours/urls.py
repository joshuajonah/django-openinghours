from django.conf.urls import url

from .views import CurrentOpeningsView

urlpatterns = [
    url(r'^$', CurrentOpeningsView.as_view(), name='openinghours_current_openings'),
]
