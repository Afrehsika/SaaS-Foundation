from django.shortcuts import render
from visits.models import PageVisit

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.conf import settings


LOGIN_URL = settings.LOGIN_URL


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

VALID_CODE = "abc123"

def pw_protected_view(request, *args, **kwargs):
    is_allowed = request.session.get('protected_page_allowed') or 0
    # print(request.session.get('protected_page_allowed'), type(request.session.get('protected_page_allowed')))
    if request.method == "POST":
        user_pw_sent = request.POST.get("code") or None
        if user_pw_sent == VALID_CODE:
            is_allowed = 1
            request.session['protected_page_allowed'] = is_allowed
    if is_allowed:
        return render(request, "protected/view.html", {})
    return render(request, "protected/entry.html", {})



@login_required
def user_only_view(request, *args, **kwargs):
    # print(request.user.is_staff)
    return render(request, "protected/user-only.html", {})


@staff_member_required(login_url=LOGIN_URL)
def staff_only_view(request, *args, **kwargs):
    return render(request, "protected/user-only.html", {})