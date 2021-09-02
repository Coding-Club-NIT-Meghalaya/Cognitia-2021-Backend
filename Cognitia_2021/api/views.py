from django.shortcuts import render
from rest_framework import viewsets
from .models import Year, Event, Prize, TeamMember
from .serializers import YearSerializer, EventSerializer, PrizeSerializer, TeamMemberSerializer
from django.db.models import CharField, Value, ForeignKey, query

# Create your views here.


class YearView(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer


class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        query_set = Event.objects.all()
        return query_set


class PrizeView(viewsets.ModelViewSet):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer


class TeamMemberView(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    filterset_fields = ['event_name']
