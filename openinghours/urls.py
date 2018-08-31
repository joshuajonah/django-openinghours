from django.conf.urls import url

from .views import currentOpenings

urlpatterns = [
    url(r'^$', currentOpenings, name='openinghours_current_openings'),
]
