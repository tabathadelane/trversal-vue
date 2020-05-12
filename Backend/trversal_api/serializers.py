from trversal_app.models import Trip
from rest_framework import serializers


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('pk',  'name', 'date',  )
