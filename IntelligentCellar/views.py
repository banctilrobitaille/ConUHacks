from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render
from form import BottleForm
from models import Cellar
from models import Bottle
from models import Crawler
from scrapyd_api import ScrapydAPI
import time
# Create your views here.

scrapyd = ScrapydAPI('http://localhost:6800')



def index(request):

    cellar = Cellar.objects.filter(name="Test", isConfigured=False)
    context_dict = {'Cellar': cellar}

    return render(request,'IntelligentCellar/index.html', context_dict)


def myCellar(request):

    cellar = Cellar.objects.filter(name="Test", isConfigured=False)
    context_dict = {'Cellar': cellar}

    return render(request,'IntelligentCellar/mycellar.html', context_dict)


def addBottle(request):

    context_dict = {}
    if request.method == 'POST':
        cup = request.POST.get('cup', '')
        crawler = Crawler.objects.all()[0]
        crawler.cup = request.POST.get('cup', '')
        crawler.save()
        scrapyd.schedule('firstapp','SAQ')
        time.sleep(3)
        context_dict['bottles'] = Bottle.objects.all()#filter(cup=cup)
        context_dict['crawler'] = crawler
        #Bottle.objects.all().delete()

    context_dict['BottleForm'] = BottleForm()

    return render(request, 'IntelligentCellar/addBottles.html', context_dict)


def inventory(request):

    context_dict = {}

    if request.method == 'POST':
        pass

    else:

        context_dict['countries'] = Bottle.objects.values('country').distinct()
        context_dict['bottles'] = Bottle.objects.all()

    return render(request, 'IntelligentCellar/inventory.html', context_dict)
