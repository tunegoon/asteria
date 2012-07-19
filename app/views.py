from django.core.context_processors import csrf
from django.shortcuts import render
from app.models import Name


def home(request):
    names = Name.objects.all()
    c = {'names': names}
    if request.method == 'POST':
        first = request.POST.get('first')
        if first:
            name = Name()
            name.first = first
            name.save()
    c.update(csrf(request))
    return render(request, 'home.html', c)
