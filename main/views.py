from django.shortcuts import render
from main.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
#from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from datetime import *
import random
import string
#def home(request):
#    tovars = Item.objects.all()
#    context = {
#        'title': 'Helloworld',
#        'tovars': tovars
#    }
#    return HttpResponse(render_to_string('index.html', context))

def home(request):
    category = Category.objects.all()
    brend = Brend.objects.all()
    context = {
        'sitename': 'Интернет-магазин',
        'categories': category,
        'brends': brend,
    }
    return HttpResponse(render_to_string('home.html', context))

def item(request, alias):
    try:
        tovar = Item.objects.get(alias=alias)
    except:
        raise Http404('Страница не найдена')
    context = {

        'tovar': tovar
    }
    return HttpResponse(render_to_string('item.html', context))

def get_category(request, alias):
    try:
        category = Category.objects.get(alias=alias)
        categories = Category.objects.all()
        tovars = Item.objects.filter(category=category)
    except:
        raise Http404('Страница не найдена')
    context = {
        'sitename': 'Интернет-магазин',
        'tovars': tovars,
        'category': category,
        'categories': categories,
    }
    return HttpResponse(render_to_string('index.html', context))

def get_brend(request, alias):
    categories = Category.objects.all()

    try:

        brend = Brend.objects.get(alias=alias)
        tovars = Item.objects.filter(brend=brend)
    except:
        raise Http404('Страница не найдена')

    context = {
        'sitename': 'Интернет-магазин',
        'categories': categories,
        'tovars': tovars,
        'brend': brend,
    }
    return HttpResponse(render_to_string('brend.html', context))

def order(request):

    context = {
    }
    return HttpResponse(render_to_string('korzina.html', context))


# Create your views here.
