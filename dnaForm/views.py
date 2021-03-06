from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import SequenceSearch
from django.utils import timezone
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers

# this is called every 0.5 seconds from the frontend to get new results
def getResults(request):
    latest_search_list = SequenceSearch.objects.order_by('-search_timestamp')[:5]
    data = serializers.serialize("json", latest_search_list)
    return JsonResponse(data, safe=False)

def index(request):
    latest_search_list = SequenceSearch.objects.order_by('-search_timestamp')[:5]
    template = loader.get_template('dnaForm/index.html')
    context = { 'latest_search_list': latest_search_list }
    return render(request, 'dnaForm/index.html', context)

def detail(request, sequence_search_id):
    search = get_object_or_404(SequenceSearch, pk=sequence_search_id)
    return render(request, 'dnaForm/detail.html', {'search': search})


def start(request):
    try :
        sequence = SequenceSearch.clean(request.POST['seq'])
        search = SequenceSearch(sequence=sequence,
                                search_timestamp=timezone.now(),
                                protein_sequence="-",
                                protein_name="-",
                                position=-1,
                                still_running=True)
        search.save()
        SequenceSearch.runSearch.delay(search.id)

    except Exception as ex:
        latest_search_list = SequenceSearch.objects.order_by('-search_timestamp')[:5]
        context = { 'latest_search_list': latest_search_list,
                    'error_message': repr(ex) }
        return render(request, 'dnaForm/index.html', context)
    return redirect('/')
