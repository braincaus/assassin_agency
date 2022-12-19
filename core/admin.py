from django.contrib import admin

from core.models import Hitman, Hit, HitStatus


# Register your models here.


@admin.register(HitStatus)
class HitStatus(admin.ModelAdmin):
    pass


@admin.register(Hitman)
class HitmanAdmin(admin.ModelAdmin):
    list_display = ['user', 'manager', 'active', ]
    raw_id_fields = ['user', 'manager', ]
    # list_filter = ['manager', 'active', ]


@admin.register(Hit)
class HitAdmin(admin.ModelAdmin):
    list_display = ['id', 'hitman', 'status', ]
    raw_id_fields = ['hitman', ]

