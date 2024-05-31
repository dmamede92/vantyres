"""
    @author: David Mamede
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from .forms import BrandForm
from .forms import BrandFormEdit
from .models import Brand


@login_required
def list(request):
    nome = request.GET.get('name_filter')

    brands = Brand.objects.all().order_by('-created_at')

    if nome:
        brands = brands.filter(name__icontains=nome)

    paginator = Paginator(brands, 4)
    page = request.GET.get('page')

    brands = paginator.get_page(page)

    return render(request, 'crud_brands/list.html', {'brands': brands})

@login_required
def edit(request, id):
    brand = get_object_or_404(Brand, pk=id)
    form = BrandFormEdit(instance=brand)

    if request.method == 'POST':
        form = BrandFormEdit(request.POST, instance=brand)

        if form.is_valid():
            brand.save()
            messages.info(request, 'Marca Atualizada com sucesso')
            return redirect('/brands')
        else:
            return render(request, 'crud_brands/edit.html', {'form': form, 'brand': brand})
    else:
        return render(request, 'crud_brands/edit.html', {'form': form, 'brand': brand})


@login_required
def delete(request, id):
    brand = get_object_or_404(Brand, pk=id)
    brand.delete()

    messages.info(request, 'Marca Deleteada com sucesso')
    return redirect('/brands')


@login_required
def new(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)

        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()

            messages.info(request, 'Marca criada com sucesso')

            return redirect('/brands')
    else:
        form = BrandForm()

    return render(request, 'crud_brands/add.html', {'form': form})
