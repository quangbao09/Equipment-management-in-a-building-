from django.contrib import admin
from .models import LOAI, PHONG, NHACUNGCAP, THIETBI

# Register your models here.
admin.site.register(LOAI)
admin.site.register(PHONG)
admin.site.register(NHACUNGCAP)
admin.site.register(THIETBI)