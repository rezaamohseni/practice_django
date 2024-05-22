from django.contrib import admin
from .models import Team , Portfolio , Skill , Service


class SkillAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Team)
admin.site.register(Portfolio)
admin.site.register(Skill,SkillAdmin)
admin.site.register(Service)

# # Register your models here.
