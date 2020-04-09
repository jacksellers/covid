from django.shortcuts import render
from django.db.models import Sum
from datetime import datetime

from data.models import Report
from website.map import generate_plot_div


def index(request, region=None):
    # plot_div = generate_plot_div()
    # context = {'plot': plot_div}
    if not region:
        region = 'Global'
    file_name = Report.objects.values_list('file_name').last()[0]
    

    """
    total = Report.objects.aggregate(Sum('confirmed'))['confirmed__sum']
    deaths = Report.objects.aggregate(Sum('deaths'))['deaths__sum']
    recovered = Report.objects.aggregate(Sum('recovered'))['recovered__sum']
    """
    context = {
        'region': region,
        'total': '{:,}'.format(total),
        'active': '{:,}'.format(total - deaths - recovered),
        'deaths': '{:,}'.format(deaths),
        'recovered': '{:,}'.format(recovered)
    }
    return render(request, 'website/index.html', context)


def api(request):
    context = {}
    return render(request, 'website/api.html', context)
