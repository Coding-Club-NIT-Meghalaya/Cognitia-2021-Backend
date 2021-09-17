from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from .models import Notification, Year, Event, TeamMember, Gallery
from .serializers import NotificationSerializer, YearSerializer, EventSerializer, TeamMemberSerializer, GallerySerializer
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
    filterset_fields = ['year', 'type']
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        query_set = Event.objects.all().order_by('start_date')
        return query_set


class TeamMemberView(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    filterset_fields = ['event_name', 'type']
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class GalleryView(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class NotificationView(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
