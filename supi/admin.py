from .models import zhuanye,student
from django.contrib import admin

class zhuanyeAdmin(admin.ModelAdmin):
    list_display=['pk','zname','zgirlnum','zboynum','isDelete']
    list_filter=['zname']
    search_fields=['zname']
    list_per_page=6


    fieldsets=[
        ("num",{"fields":['zgirlnum','zboynum']}),
        ("base",{"fields":['zname','isDelete',]})
    ]


admin .site.register(zhuanye,zhuanyeAdmin)
admin .site.register(student)

