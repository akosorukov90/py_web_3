from rest_framework import serializers
from measurements.models import Project, Measurement


class ProjectSerializer(serializers.ModelSerializer):
    #text = serializers.CharField(required=True)

    class Meta:
        model = Project
        fields = 'id', 'name', 'latitude', 'longitude'


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = 'id', 'value', 'project', 'updated_at'
