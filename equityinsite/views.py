from django.shortcuts import render, redirect
from indexes.models import nifty_50, nifty_next, nifty_midcap, nifty_smallcap, nifty_auto
from indexes.models import nifty_bank, nifty_finance, nifty_psu_bank, nifty_it, nifty_metal, nifty_pharma
from indexes.analysis import analysis
from registration import views
from django.contrib.auth.decorators import login_required

def page_name(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        print(name, email)

def home(request):
    nifty_50_data = nifty_50.objects.all()
    nifty_next_data = nifty_next.objects.all()
    nifty_midcap_data = nifty_midcap.objects.all()
    nifty_smallcap_data = nifty_smallcap.objects.all()
    nifty_bank_data = nifty_bank.objects.all()
    nifty_finance_data = nifty_finance.objects.all()
    nifty_psu_bank_data = nifty_psu_bank.objects.all()
    nifty_it_data = nifty_it.objects.all()
    nifty_auto_data = nifty_auto.objects.all()
    nifty_metal_data = nifty_metal.objects.all()
    nifty_pharma_data = nifty_pharma.objects.all()

    data = {
        'nifty_50': nifty_50_data,
        'nifty_next': nifty_next_data,
        'nifty_midcap': nifty_midcap_data,
        'nifty_smallcap': nifty_smallcap_data,
        'nifty_bank': nifty_bank_data,
        'nifty_finance': nifty_finance_data,
        'nifty_psu_bank': nifty_psu_bank_data,
        'nifty_it': nifty_it_data,
        'nifty_auto': nifty_auto_data,
        'nifty_metal': nifty_metal_data,
        'nifty_pharma': nifty_pharma_data
    }
    return render(request, "index.html", data)

def analysis_page(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if 'name' in request.GET:
            symbol = request.GET['name']
            data = analysis(symbol)
    return render(request, "analysis.html", data)

def signup_page(request):
    return views.signup_page(request)

def login_page(request):
    return views.login_page(request)

def logout_page(request):
    return views.logout_page(request)

def header(request):
    if request.method == 'POST':
        company = request.POST['company']
        print(company)
        data = {"company": company}
    return render(request, "header.html", data)

def test(request):
    return render(request, "test.html")