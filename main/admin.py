from django.contrib import admin
from django.contrib.auth.models import User,Group
from .models import *

admin.site.unregister(User)
admin.site.unregister(Group)

class IncorrectInline(admin.StackedInline):
    model = Incorrect
    extra = 1



@admin.register(Correct)
class CorrectAdmin(admin.ModelAdmin):
    inlines = [IncorrectInline]


@admin.register(Incorrect)
class IncorrectAdmin(admin.ModelAdmin):
    pass



