from django.contrib import admin

from .models import Board, Flyer, Office

@admin.register(Board)
class BoardBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', 'status')

@admin.register(Flyer)
class FlyerBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_boards',)

    def get_boards(self, obj):
        return "\n".join([b.name for b in obj.board.all()])

@admin.register(Office)
class OfficeBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location', )