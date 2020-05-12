from .serializers import TripSerializer
from trversal_app.models import Trip

from rest_framework import generics, viewsets

class TripViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsCreatorOrReadOnlyTrip,)
  
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
