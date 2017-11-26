from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.SuitsView.as_view(), name='suits'),
]