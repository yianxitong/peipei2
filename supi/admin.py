from django.contrib import admin
from .models import zhuanye,student


class zhuanyeAdmin(admin.ModelAdmin):
    list_display=['pk','zname','zgirlnum','zboynum','isDelete','school']
    list_filter=['zname']
    search_fields=['zname']
    list_per_page=7


    fieldsets=[
        ("base",{"fields":['zname','isDelete',]}),
        ("num",{"fields":['zgirlnum','zboynum']})
    ]
admin.site.register(zhuanye,zhuanyeAdmin)

class studentsAdmin(admin.ModelAdmin):

    def gender(self):
        if self.sgender:
            return"男"
        else:
            return"女"
    list_display=['sid','sname','zhuanye',gender,'school','isDelete']
    list_filter=['sname']
    search_fields=['sname']
    list_per_page=6
admin.site.register(student,studentsAdmin)

