from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from travello.models import Destination

# Create your views here.
def index(request):
    # dest1 = Destination()
    # dest1.name = 'Coimbatore'
    # dest1.price =900
    # dest1.desc = 'City that Never Sleeps'
    # dest1.img = 'destination_1.jpg'
    # dest1.off = False


    # dest2 = Destination()
    # dest2.name = 'Banglore'
    # dest2.price =1000
    # dest2.desc = 'Electronic City'
    # dest2.img = 'destination_2.jpg'
    # dest2.off = True


    # dest3 = Destination()
    # dest3.name = 'Chennai'
    # dest3.price =1500
    # dest3.desc = ' Marina Beach '
    # dest3.img = 'destination_3.jpg'
    # dest3.off = True


    # dests=[ dest1, dest2, dest3]

    dests = Destination.objects.all()

    context={
        'dests' : dests
    }
    template = loader.get_template('index.html')
    
    # return HttpResponse(template.render())
    return HttpResponse(template.render(context, request))
