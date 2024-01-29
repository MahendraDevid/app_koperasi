from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Anggota(models.Model):
    nama = models.CharField(max_length=255,blank=True, null=True)
    alamat = models.TextField(max_length=255,blank=True, null=True)
    no_telepon = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    tgl_gabung = models.DateField()
    # sekolah =

    # default
    # create_by = 
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama
    
    
    class Meta:
        db_table = "anggota"
        ordering = ["-id"]
        verbose_name_plural = "anggota"