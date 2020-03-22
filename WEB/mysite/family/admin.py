from django.contrib import admin
from .models import Family, Hobby
# Register your models here.
class HobbyInline(admin.TabularInline):
    model = Hobby
    extra = 3

class FamilyAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,                      {'fields': ['id']}),
    #     (None,                      {'fields': ['name']}),
    #     ('Date information',        {'fields': ['age']})
    # ]
    inlines = [HobbyInline]
    list_display = ('id', 'name', 'age')
    list_filter = ['age']
    search_fields = ['name']

admin.site.register(Family, FamilyAdmin)