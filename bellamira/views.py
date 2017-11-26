from django.shortcuts import render
from django.views import generic
from .models import Suit

class SuitsView(generic.ListView):
    template_name = 'bellamira/suits.html'
    context_object_name = 'suits_list'

    def get_queryset(self):
        return Suit.objects.all()
