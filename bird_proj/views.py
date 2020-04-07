from django.shortcuts import render, redirect
from .models import Site, Bird
from django.forms import inlineformset_factory, modelform_factory

def index(request, pk):
    site = Site.objects.get(entry_id=pk)
    BirdFormset = inlineformset_factory(Site, Bird, exclude=(), extra=10)
    SiteForm = modelform_factory(Site, exclude=())

    if request.method == 'POST':
        site_form = SiteForm(request.POST, instance=site)
        formset = BirdFormset(request.POST, instance=site)
        if formset.is_valid() and site_form.is_valid():
            site_form.save()
            formset.save()

            return redirect('index', pk=site.pk)

    formset = BirdFormset(instance=site)
    site_form = SiteForm(instance=site)

    return render(request, 'bird_proj/index.html',
        {'formset' : formset, 'site_form':site_form})
