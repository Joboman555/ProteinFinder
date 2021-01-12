from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import SequenceSearch
from django.utils import timezone
from django.urls import reverse


def index(request):
    latest_search_list = SequenceSearch.objects.order_by('-search_timestamp')[:5]
    template = loader.get_template('dnaForm/index.html')
    context = { 'latest_search_list': latest_search_list }
    return render(request, 'dnaForm/index.html', context)

def detail(request, sequence_search_id):
    search = get_object_or_404(SequenceSearch, pk=sequence_search_id)
    return render(request, 'dnaForm/detail.html', {'search': search})

def start(request):
    search = SequenceSearch(sequence=request.POST['seq'], search_timestamp=timezone.now())
    search.save()
    return redirect('/form/')