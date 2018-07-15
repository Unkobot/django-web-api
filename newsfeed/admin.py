from django.contrib import admin
from .models import Newsfeed
# Register your models here.
class NewsfeedAdmin(admin.ModelAdmin):
    readonly_fields = ('author',)
admin.site.register(Newsfeed, NewsfeedAdmin)