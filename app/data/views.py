from rest_framework import generics
from rest_framework import filters as rest_filters
from django_filters import rest_framework as filters

from data.models import Report
from data.serializers import ReportSerializer


class ReportFilter(filters.FilterSet):
    file_name = filters.CharFilter(
        field_name='file_name', lookup_expr='exact'
    )
    city = filters.CharFilter(field_name='city', lookup_expr='exact')
    state = filters.CharFilter(field_name='state', lookup_expr='exact')
    region = filters.CharFilter(field_name='region', lookup_expr='exact')
    confirmed__gt = filters.NumberFilter(
        field_name='confirmed', lookup_expr='gt'
    )
    confirmed__lt = filters.NumberFilter(
        field_name='confirmed', lookup_expr='lt'
    )
    deaths__gt = filters.NumberFilter(
        field_name='deaths', lookup_expr='gt'
    )
    deaths__lt = filters.NumberFilter(
        field_name='deaths', lookup_expr='lt'
    )
    recovered__gt = filters.NumberFilter(
        field_name='recovered', lookup_expr='gt'
    )
    recovered__lt = filters.NumberFilter(
        field_name='recovered', lookup_expr='lt'
    )

    class Meta:
        model = Report
        fields = [
            'file_name', 'city', 'state', 'region', 'confirmed',
            'deaths', 'recovered'
        ]


class ListReportView(generics.ListAPIView):
    """List reports."""
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    filter_backends = (
        filters.DjangoFilterBackend,
        rest_filters.SearchFilter,
        rest_filters.OrderingFilter,
    )
    filterset_class = ReportFilter
    search_fields = [
        'file_name', 'city', 'state', 'region', 'confirmed', 'deaths',
        'recovered'
    ]
    ordering_fields = [
        'file_name', 'city', 'state', 'region', 'confirmed', 'deaths',
        'recovered'
    ]
