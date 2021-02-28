from django.contrib import admin
from .models import Complain

# Register your models here.


class MyAdmin(admin.ModelAdmin):
    # list_display_links = None
    # fields = ['private']
    list_display = ('id', 'status','user','date','private')
    change_list_template = 'change_list_graph.html'

    def has_add_permission(self, request, obj=None):
        return False

    # def has_change_permission(self, request, obj=None):
    #     return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_readonly_fields(self, request, obj=None):
        if obj:  # when editing an object
            return ['image', 'description', 'private', 'tag', 'user']
        return self.readonly_fields

admin.site.register(Complain, MyAdmin)


