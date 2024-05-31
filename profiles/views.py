"""
    @author: David Mamede
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from .forms import ProfileForm
from .forms import ProfileFormEdit
from .models import Profile


@login_required
def list(request):
    nome = request.GET.get('name_filter')
    status = request.GET.get('status_filter')

    profiles = Profile.objects.all().order_by('-created_at')

    if nome:
        profiles = profiles.filter(name__icontains=nome)
    if status:
        profiles = profiles.filter(status=status)

    paginator = Paginator(profiles, 4)
    page = request.GET.get('page')

    profiles = paginator.get_page(page)

    return render(request, 'crud_profiles/list.html', {'profiles': profiles})

@login_required
def edit(request, id):
    profile = get_object_or_404(Profile, pk=id)
    form = ProfileFormEdit(instance=profile)

    if request.method == 'POST':
        form = ProfileFormEdit(request.POST, instance=profile)

        if form.is_valid():
            profile.save()
            messages.info(request, 'Profile Atualizado com sucesso')
            return redirect('/profiles')
        else:
            return render(request, 'crud_profiles/edit.html', {'form': form, 'profile': profile})
    else:
        return render(request, 'crud_profiles/edit.html', {'form': form, 'profile': profile})


@login_required
def delete(request, id):
    profile = get_object_or_404(Profile, pk=id)
    profile.delete()

    messages.info(request, 'Profile Deleteado com sucesso')
    return redirect('/profiles')


@login_required
def new(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            # Salvando o usuário padrão
            profile = form.save(commit=False)
            profile.save()

            messages.info(request, 'Usuário criado com sucesso')

            return redirect('/profiles')
    else:
        form = ProfileForm()

    return render(request, 'crud_profiles/add.html', {'form': form})
