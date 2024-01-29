from django.contrib import admin
from .models import Anggota

class AnggotaAdmin(admin.ModelAdmin):
    list_display = ['nama','alamat', 'no_telepon' , 'email','tgl_gabung',]

admin.site.register(Anggota, AnggotaAdmin)