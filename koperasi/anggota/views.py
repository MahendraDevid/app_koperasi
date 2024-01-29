from django.shortcuts import render,redirect

from .forms import AnggotaForm
from .models import Anggota

def update(request, id):
     anggota_update = Anggota.objects.get(pk= id)
    
     data = {       
         'nama':  anggota_update.nama,
         'alamat': anggota_update.alamat,
         'no_telepon': anggota_update.no_telepon,
         'email': anggota_update.email,
         'tgl_gabung': anggota_update.tgl_gabung,
     }
    
     anggota_form = AnggotaForm(request.POST or None, initial=data, instance=anggota_update)
    
     if request.method == 'POST':
         if anggota_form.is_valid():
             anggota_form.save()
            
         return redirect('anggota:list')
    
     context = {
         "anggota_form": anggota_form,
     }
            
     return render(request, 'anggota/create.html', context)

def delete(request, id):
    Anggota.objects.get(pk=id).delete()
    return redirect('anggota:list')

def create(request):
    anggota_form = AnggotaForm(request.POST or None)
    
    if request.method == 'POST':
        if anggota_form.is_valid():
            anggota_form.save()
            
        return redirect('anggota:list')
    
    context = {
        "anggota_form": anggota_form,
    }
            
    return render(request, 'anggota/create.html', context)

def list(request):
    anggota_list = Anggota.objects.all()
    return render(request, 'anggota/anggota.html', {'anggota_list': anggota_list})