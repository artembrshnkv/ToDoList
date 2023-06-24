from django.contrib import admin
from .models import *


class RubricAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Rubric, RubricAdmin)

