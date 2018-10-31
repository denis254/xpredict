from django.shortcuts import render, redirect

from django.views.generic import TemplateView

from . models import FreeTipsGames, VipTips, PunterPick, RollOver

from django.utils import timezone

from . forms import RegistrationForm

from django.contrib import messages

def play(request):
    return redirect("https://play.google.com/store/apps/details?id=com.a1xpredict.a1xpredict")

def optout(request):
    return redirect("http://www.crafttechsolution.com/")

def home(request):

    return redirect("http://www.predictpoa.com/")

def androidapp(request):

    template_name = 'androidapp.html'

    return render(request, 'androidapp.html')

def information(request):

    template_name = 'information.html'

    return render(request, 'information.html')


def rollover(request):

    template_name = 'rollover.html'

    return render(request, 'rollover.html')

def viptips(request):

    template_name = 'viptips.html'

    return render(request, 'viptips.html')

def privacy(request):

    template_name = 'privacy.html'

    return render(request, 'privacy.html')

def contactus(request):

    template_name = 'contactus.html'

    return render(request, 'palsbet/contactus.html')

def guide(request):

    template_name = 'guide.html'

    return render(request, 'guide.html')

def backToHomePage(request):

    template_name = 'backtohomepage.html'

    return render(request, 'palsbet/backtohomepage.html')

def viewolderesults(request):

    template_name = 'older_results.html'

    args = {}

    older_results_teams = FreeTipsGames.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[10:60]


    args ['older_results_teams'] = grouped(older_results_teams, 10)

    return render(request, 'older_results.html', args)

def howmanyodds(request):

    template_name = 'howmanyodds.html'

    return render(request, 'howmanyodds.html')

def modeofsending(request):

    template_name = 'modeofsending.html'

    return render(request, 'modeofsending.html')

def timeofsending(request):

    template_name = 'timeofsending.html'

    return render(request, 'timeofsending.html')


def homeviptips(request):

    model = VipTips

    template_name = 'homeviptips.html'

    args = {}

    vip_tips = VipTips.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:3]


    args ['vip_tips'] = vip_tips

    return render(request, 'homeviptips.html', args)


def punterpick(request):

    model = PunterPick

    template_name = 'punterpick.html'

    args = {}

    punterpick = PunterPick.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:3]


    args ['punterpick'] = punterpick

    return render(request, 'punterpick.html', args)


def rolloverh(request):

    model = RollOver

    template_name = 'viprollover.html'

    args = {}

    rollover = RollOver.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:4]


    args ['rollover'] = rollover

    return render(request, 'viprollover.html', args)

def payment(request):

    template_name = 'payment.html'

    return render(request, 'payment.html')

def grouped(l, n):
    for i in range(0, len(l), n):
        yield l[i:i+n]



def homevip(request):

    template_name = 'home_vip.html'

    return render(request, 'home_vip.html')

def register(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            user.save()


            messages.success(request, 'Registration successful.Recharge your account to access our vip services')

            return redirect('/information/')

    else:
        form = RegistrationForm()


    return render(request, 'account/register.html', {'form':form})
