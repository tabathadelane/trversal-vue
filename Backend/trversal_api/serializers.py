from rest_framework import serializers
from trversal_app.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = ('pk',  'name', 'date',  )
