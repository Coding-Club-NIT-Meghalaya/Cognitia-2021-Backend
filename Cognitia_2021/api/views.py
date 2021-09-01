from django.shortcuts import render
from rest_framework import viewsets
from .models import Year, Event, Prize, TeamMember
from .serializers import YearSerializer, EventSerializer, PrizeSerializer, TeamMemberSerializer

# Create your views here.


class YearView(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer


class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class PrizeView(viewsets.ModelViewSet):
    queryset = Prize.objects.all()
    serializer_class = PrizeSerializer


class TeamMemberView(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
