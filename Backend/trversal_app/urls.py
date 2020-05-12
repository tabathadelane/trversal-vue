from django.urls import path
from . import views

app_name = 'trversal' # for namespacing
urlpatterns = [
    path('trip/', views.TripListView.as_view()),
    path('trip/<int:pk/', views.TripDetailView.as_view()),
]
