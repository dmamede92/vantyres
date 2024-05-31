"""
    @author: David Mamede
"""
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from datetime import datetime
from profiles.models import Profile
from utils import constants
from .forms import CustomAuthenticationForm, UsuarioFormEdit
from .forms import UsuarioForm
from .models import Usuario


def custom_logout(request):
    logout(request)
    return redirect(constants.ROUTE['login'])


def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('username')
            senha = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=senha)

            if user is not None:
                if user.status != 'ati':
                    messages.warning(request, 'Usuario Desativado')

                else:
                    login(request, user)
                    return redirect(constants.ROUTE['users'])  # redirecionar para a página de dashboard após o login
    else:
        form = CustomAuthenticationForm()

    return render(request, f'{constants.CRUD_PATH["users"]}/{constants.FORMS["login"]}', {'form': form})


@login_required
def list(request):
    nome = request.GET.get('name_filter')
    email = request.GET.get('email_filter')
    status = request.GET.get('status_filter')

    usuarios = Usuario.objects.all().order_by('-created_at')

    if nome:
        usuarios = usuarios.filter(nome__icontains=nome)
    if email:
        usuarios = usuarios.filter(email__icontains=email)
    if status:
        usuarios = usuarios.filter(status=status)

    paginator = Paginator(usuarios, 4)
    page = request.GET.get('page')
    usuarios = paginator.get_page(page)

    return render(request, f'{constants.CRUD_PATH["users"]}/{constants.FORMS["list"]}', {'usuarios': usuarios})


@login_required
def edit(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    form = UsuarioFormEdit(instance=usuario)

    if request.method == 'POST':
        try:
            data_nascimento_str = request.POST.get('data_nascimento')
            data_nascimento_formatada = datetime.strptime(data_nascimento_str, '%d/%m/%Y').strftime('%Y-%m-%d')

        except:
            messages.warning(request, 'Data de nascimento inválida')
            return render(request, f'{constants.CRUD_PATH["users"]}/{constants.FORMS["edit"]}', {'form': form, 'usuario': usuario})

        mutable_post_data = request.POST.copy()

        mutable_post_data['data_nascimento'] = data_nascimento_formatada
        form = UsuarioFormEdit(mutable_post_data, instance=usuario)

        if form.is_valid():
            usuario = form.save(commit=False)

            perfil_id = request.POST.get('profiles')
            usuario.profiles_id = perfil_id

            usuario.save()
            messages.info(request, 'Usuário atualizado com sucesso')
            return redirect(constants.ROUTE['users'])
        else:
            return render(request, f'{constants.CRUD_PATH["users"]}/{constants.FORMS["edit"]}',
                          {'form': form, 'usuario': usuario})
    else:
        return render(request, f'{constants.CRUD_PATH["users"]}/{constants.FORMS["edit"]}',
                      {'form': form, 'usuario': usuario})


@login_required
def delete(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    usuario.delete()

    messages.info(request, 'Usuario Deleteado com sucesso')
    return redirect(constants.ROUTE['users'])


@login_required
def new(request):
    if request.method == 'POST':

        try:
            data_nascimento_str = request.POST.get('data_nascimento')
            data_nascimento_formatada = datetime.strptime(data_nascimento_str, '%d/%m/%Y').strftime('%Y-%m-%d')

        except ValueError:
            messages.warning(request, 'Data de nascimento inválida')
            form = UsuarioForm(request.POST)

            profiles = Profile.objects.all().order_by('-created_at')
            return render(request, f'{constants.CRUD_PATH["users"]}/{constants.FORMS["add"]}',
                          {'form': form, 'profiles': profiles, 'tipos': Usuario.TIPO})

        mutable_post_data = request.POST.copy()
        mutable_post_data['data_nascimento'] = data_nascimento_formatada
        form = UsuarioForm(mutable_post_data)

        if form.is_valid():
            usuario = form.save(commit=False)

            usuario.password = make_password(usuario.password)

            usuario.tipo = mutable_post_data.get('tipo')
            usuario.profiles_id = mutable_post_data.get('profiles')

            usuario.save()

            messages.info(request, 'Usuário criado com sucesso')
            return redirect(constants.ROUTE['users'])
        else:
            profiles = Profile.objects.all().order_by('-created_at')

            return render(request, f'{constants.CRUD_PATH["users"]}/{constants.FORMS["add"]}',
                          {'form': form, 'profiles': profiles, 'tipos': Usuario.TIPO})
    else:
        form = UsuarioForm()
        profiles = Profile.objects.all().order_by('-created_at')

        return render(request, f'{constants.CRUD_PATH["users"]}/{constants.FORMS["add"]}',
                      {'form': form, 'profiles': profiles, 'tipos': Usuario.TIPO})
