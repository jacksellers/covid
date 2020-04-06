from django.shortcuts import render
from django.db.models import Sum

from data.models import Report
from website.map import generate_plot_div


def index(request, region='global'):
    # plot_div = generate_plot_div()
    # context = {'plot': plot_div}
    confirmed_sum = Report.objects.aggregate(Sum('confirmed'))
    deaths_sum = Report.objects.aggregate(Sum('deaths'))
    recovered_sum = Report.objects.aggregate(Sum('recovered'))
    context = {
        'region': region.upper(),
        'confirmed_sum': confirmed_sum,
        'deaths_sum': deaths_sum,
        'recovered_sum': recovered_sum
    }
    print(context)
    return render(request, 'website/index.html', context)


def api(request):
    context = {}
    return render(request, 'website/api.html', context)
