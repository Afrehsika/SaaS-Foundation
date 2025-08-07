from django.shortcuts import render
from visits.models import PageVisit


def home(request,*args, **kwargs):
    if request.user.is_authenticated:
        print(request.user.first_name)
    return about(request, *args, **kwargs)


def about(request, *args, **kwargs):
    qr = PageVisit.objects.filter(path=request.path)
    qr_total =PageVisit.objects.all()
    PageVisit.objects.create(path=request.path)
    try: 
        percentage = (qr.count() / qr_total.count()) * 100
    except ZeroDivisionError:
        percentage = 0
    
    context = {
        'name': 'Kriss Ntim',
        'page_visit': qr.count(),
        'total_page_visits': qr_total.count(),
        'percentage': percentage,
    }
    return render(request, 'home.html', context)