from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk
from .forms import ProdukForm
from django.contrib import messages

def produk_list(request):
    produk = Produk.objects.all()
    return render(request, 'produk/list.html', {'produk': produk})

def produk_create(request):
    form = ProdukForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Produk berhasil ditambahkan!')
        return redirect('produk_list')
    return render(request, 'produk/form.html', {'form': form})

def produk_update(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    form = ProdukForm(request.POST or None, instance=produk)
    if form.is_valid():
        form.save()
        messages.success(request, 'Produk berhasil diperbarui!')
        return redirect('produk_list')
    return render(request, 'produk/form.html', {'form': form})

def produk_delete(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    produk.delete()
    messages.success(request, 'Produk berhasil dihapus!')
    return redirect('produk_list')
