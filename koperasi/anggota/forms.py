from django import forms
from .models import Anggota

class AnggotaForm(forms.ModelForm):
   class Meta:
       model = Anggota
       fields = ['nama',
                 'alamat',
                 'no_telepon',
                 'email',
                 'tanggal_lahir',]