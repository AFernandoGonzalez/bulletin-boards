from django.contrib import admin

from .models import Board

@admin.register(Board)
class BoardBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'status')