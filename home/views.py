from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
import datetime as pt

n = pt.datetime.now()
# Create your views here.
def timeDis(request):
  context = {
    'date': n.strftime("%b-%d-%y"),
    'time': n.strftime("%I:%M %p")
  }

  return render(request, 'index.html', context)