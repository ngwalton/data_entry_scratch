from django.shortcuts import render, redirect
from .models import Site, Bird
from django.forms import inlineformset_factory, modelform_factory #, SplitDateTimeWidget
from django.contrib.auth.decorators import login_required
# from django.contrib.admin.widgets import AdminSplitDateTime

@login_required
def index(request, pk):
    site = Site.objects.get(entry_id=pk)
    BirdFormset = inlineformset_factory(Site, Bird, exclude=(), extra=10)
    SiteForm = modelform_factory(Site, exclude=()) #,
        # widgets={"day": SplitDateTimeWidget(date_format='%m/%d/%Y', time_format='%H:%M')})

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

@login_required
def new(request, pk=None):
    site = Site()  # new/empty Site object
    BirdFormset = inlineformset_factory(Site, Bird, exclude=(), extra=10)
    SiteForm = modelform_factory(Site, exclude=()) #, widgets={"day": SplitDateTimeWidget()})

    if request.method == 'POST':
        site_form = SiteForm(request.POST, instance=site)
        formset = BirdFormset(request.POST, instance=site)

        if formset.is_valid() and site_form.is_valid():
            site_obj = site_form.save()

            # for form in formset:
            #     if form.cleaned_data['quantity'] > 0:
            #         obj = form.save(commit=False)
            #         obj.entry_id = 'ticket_name'
            #         obj.save()

            formset.save()

            return redirect('index', pk=site_obj.pk)
        else:
            error_txt = "There was an error: please try again"
            return render(request, 'bird_proj/index.html',
                {'formset' : formset, 'site_form':site_form, 'error_txt':error_txt})

    # queryset = Site.objects.none()
    # formset = BirdFormset(queryset=queryset)
    # site_form = SiteForm(queryset=queryset)
    formset = BirdFormset(instance=site)
    site_form = SiteForm(instance=site)

    return render(request, 'bird_proj/index.html',
        {'formset' : formset, 'site_form':site_form})
