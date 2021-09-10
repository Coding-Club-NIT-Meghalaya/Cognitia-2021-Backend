from django.shortcuts import render
from rest_framework import viewsets
from .models import Year, Event, TeamMember
from .serializers import YearSerializer, EventSerializer, TeamMemberSerializer
from django.db.models import CharField, Value, ForeignKey, query
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class YearView(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class EventView(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    filterset_fields = ['year']
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query_set = Event.objects.all()
        return query_set


class TeamMemberView(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    filterset_fields = ['event_name']
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
