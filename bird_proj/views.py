from django.shortcuts import render, redirect
from .models import Site, Bird
from django.forms import inlineformset_factory

def index(request, site_id):
    site = Site.objects.get(entry_id=site_id)
    BirdFormset = inlineformset_factory(Site, Bird, exclude=())

    if request.method == 'POST':
        formset = BirdFormset(request.POST, instance=site)
        if formset.is_valid():
            formset.save()

            return redirect('index', site_id=site.id)

    formset = BirdFormset(instance=site)

    return render(request, 'bird_proj/index.html', {'formset' : formset})

