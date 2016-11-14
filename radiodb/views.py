from django.shortcuts import render_to_response
from django.shortcuts import HttpResponse
from django.views.generic.base import TemplateView
import datetime

from radiodb.models import MassportMaster

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    entries = MassportMaster.objects.all()
    return render_to_response('index.html', {'MassportMaster': entries[:20]})

class IndexView(TemplateView):
    template_name = 'index.html'
    