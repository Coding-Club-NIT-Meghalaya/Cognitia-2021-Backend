from django.contrib import admin
from .models import Year, Event, Prize, TeamMember

# Register your models here.


@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ['year', 'start_date', 'end_date']


@admin.register(Prize)
class PrizeAdmin(admin.ModelAdmin):
    list_display = ['scope', 'prize1',
                    'prize2', 'prize3', 'description']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date',
                    'type', 'start_time', 'duration', 'year', 'prize', 'description', 'rules', 'judging_parameter', 'registration_link', 'image']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['member_name', 'type', 'roll_no',
                    'email', 'image', 'event_name']
