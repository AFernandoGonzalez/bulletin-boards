from django.contrib import admin

from .models import Board, Flyer, Office

@admin.register(Board)
class BoardBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'status')

@admin.register(Flyer)
class FlyerBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(Office)
class OfficeBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', )