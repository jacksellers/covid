from rest_framework import serializers

from data.models import Report


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = (
            'file_name', 'city', 'state', 'region', 'last_update',
            'confirmed', 'deaths', 'recovered'
        )