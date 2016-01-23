from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Cellar
# Create your views here.


def index(request):

    cellar = Cellar.objects.filter(name="Test", isConfigured=True)

    name = cellar.count()
    context_dict = {'Name': name}
    return render_to_response('IntelligentCellar/index.html', context_dict)