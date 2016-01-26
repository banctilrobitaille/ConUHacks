from django.forms import ModelForm
from models import Bottle

class BottleForm(ModelForm):
    class Meta:
       model = Bottle
       fields = ['cup']
