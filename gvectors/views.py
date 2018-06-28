from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

from .forms import GVectorForm
from .models import GVector
from .tasks import process_gvector


# Create your views here.

def index(request):
    gvectors = GVector.objects.all()
    return render(request, "gvectors/index.html", {
        'gvectors': gvectors
    })

def create(request):
    if request.method == "POST":
        form = GVectorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gvectors_index')
    else:
        form = GVectorForm()
    return render(request, "gvectors/create.html", {
        'form': form
    })

def show(request, gvector_id):
    gvector = GVector.objects.get(id=gvector_id)
    return render(request, "gvectors/show.html", {
        'gvector': gvector
    })

def show_json(request, gvector_id):
    gvector = GVector.objects.get(id=gvector_id)
    return JsonResponse({
        'gvector': {
            'description': gvector.description,
            'is_in_queue': gvector.is_in_queue,
            'is_processing': gvector.is_processing,
            'percentage': gvector.percentage,
            'percentage_text': gvector.percentage_text,
            'created_at': gvector.created_at,
            'uploaded_at': gvector.uploaded_at,
        }
    })

def process(request, gvector_id):
    gvector = GVector.objects.get(id=gvector_id)
    gvector.is_in_queue = True
    gvector.is_processing = False
    gvector.percentage = 0
    gvector.save()
    process_gvector.delay(gvector_id)
    messages.success(request, 'Processing file #{} file! Wait a moment...'.format(gvector_id))
    return redirect('gvectors_show', gvector_id=gvector_id)

def delete(request, gvector_id):
    GVector.objects.filter(id=gvector_id).delete()
    return redirect('gvectors_index')
