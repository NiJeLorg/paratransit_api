from django.conf.urls import url
from api import views

# urls here will all be prefixed with api/

urlpatterns = [
    url(r'^$', views.api_index, name='api_index'),
]
