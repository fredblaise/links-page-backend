from django.contrib import admin
from .models import Link, LinkPage


# Register your models here.
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = Link.DisplayFields


@admin.register(LinkPage)
class LinkPageAdmin(admin.ModelAdmin):
    list_display = LinkPage.DisplayFields
