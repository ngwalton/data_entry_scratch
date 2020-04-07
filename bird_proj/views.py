from django.shortcuts import render, redirect
from .models import Site, Bird
from django.forms import inlineformset_factory

def index(request, pk):
    site = Site.objects.get(entry_id=pk)
    BirdFormset = inlineformset_factory(Site, Bird, exclude=(), extra=10)

    if request.method == 'POST':
        formset = BirdFormset(request.POST, instance=site)
        if formset.is_valid():
            formset.save()

            return redirect('index', pk=site.pk)

    formset = BirdFormset(instance=site)

    return render(request, 'bird_proj/index.html', {'formset' : formset})
