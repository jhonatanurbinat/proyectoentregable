from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

from fmembers.models import Fmembers

def create_fmember(request):
    new_fmember = Fmembers.objects.create(name='fredi',age=50,isfamily=True,relation='Padre')
    new_fmember = Fmembers.objects.create(name='Margarita',age=50,isfamily=True,relation='Madre')
    new_fmember = Fmembers.objects.create(name='Ivonne',age=30,isfamily=True,relation='Hermana')    
    print(new_fmember)
    return HttpResponse('Se creo el nuevo fmember')

def list_fmembers(request):
    all_fmembers = Fmembers.objects.all()
    context = {
        'fmembers':all_fmembers,
    }
    return render(request, 'fmembers/list_fmembers.html', context=context)
