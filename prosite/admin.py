from django.contrib import admin
from .models import *


class BlockAdmin (admin.ModelAdmin):
    list_display = ["id", "name"]


class TextAdmin (admin.ModelAdmin):
    list_display = ["id","id_block", "title", "body"]


class AlbumAdmin (admin.ModelAdmin):
    list_display = ["id", "id_block", "title", "photo"]


admin.site.register (Text, TextAdmin)
admin.site.register (Block, BlockAdmin)
admin.site.register (Album, AlbumAdmin)
