"""
    @author: David Mamede
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from utils import constants
from datetime import datetime
from .forms import ClientsForm
from .forms import ClientsFormEdit
from .forms import VehicleForm
from .models import Clients
from .models import Vehicle
from brands.models import Brand


@login_required
def list(request):
    nome = request.GET.get('nome_filter')
    email = request.GET.get('email_filter')
    status = request.GET.get('status_filter')

    clients = Clients.objects.all().order_by('-created_at')

    if nome:
        clients = clients.filter(nome__icontains=nome)
    if email:
        clients = clients.filter(email__icontains=email)
    if status:
        clients = clients.filter(status=status)

    paginator = Paginator(clients, 4)
    page = request.GET.get('page')

    clients = paginator.get_page(page)

    return render(request, f'{constants.CRUD_PATH["clients"]}/{constants.FORMS["list"]}', {'clients': clients})


@login_required
def edit(request, id):
    client = get_object_or_404(Clients, pk=id)
    form = ClientsFormEdit(instance=client)

    if request.method == 'POST':
        try:
            data_nascimento_str = request.POST.get('data_nascimento')
            data_nascimento_formatada = datetime.strptime(data_nascimento_str, '%d/%m/%Y').strftime('%Y-%m-%d')

        except:
            messages.warning(request, 'Data de nascimento inválida')
            return render(request, f'{constants.CRUD_PATH["clients"]}/{constants.FORMS["edit"]}', {'form': form, 'cliente': client})

        mutable_post_data = request.POST.copy()

        mutable_post_data['data_nascimento'] = data_nascimento_formatada
        form = ClientsFormEdit(mutable_post_data, instance=client)

        if form.is_valid():
            client = form.save(commit=False)

            perfil_id = request.POST.get('profiles')
            client.profiles_id = perfil_id

            client.save()
            messages.info(request, 'Client Atualizado com sucesso')
            return redirect(constants.ROUTE['clients'])
        else:
            return render(request, f'{constants.CRUD_PATH["clients"]}/{constants.FORMS["edit"]}',
                          {'form': form, 'client': client})
    else:
        return render(request, f'{constants.CRUD_PATH["clients"]}/{constants.FORMS["edit"]}',
                      {'form': form, 'client': client})


@login_required
def delete(request, id):
    client = get_object_or_404(Clients, pk=id)
    client.delete()

    messages.info(request, 'Client Deleteado com sucesso')
    return redirect(constants.ROUTE['clients'])


@login_required
def new(request):
    if request.method == 'POST':

        try:
            data_nascimento_str = request.POST.get('data_nascimento')
            data_nascimento_formatada = datetime.strptime(data_nascimento_str, '%d/%m/%Y').strftime('%Y-%m-%d')

        except ValueError:
            messages.warning(request, 'Data de nascimento inválida')
            mutable_post_data = request.POST.copy()
            form = ClientsForm(mutable_post_data)

            print(f"form: {form}")

            clients = Clients.objects.all().order_by('-created_at')
            return render(request, f'{constants.CRUD_PATH["clients"]}/{constants.FORMS["add"]}',
                          {'form': form, 'clients': clients, 'tipos': Clients.TIPO})

        mutable_post_data = request.POST.copy()
        mutable_post_data['data_nascimento'] = data_nascimento_formatada
        form = ClientsForm(mutable_post_data)

        if form.is_valid():
            client = form.save(commit=False)

            client.tipo = mutable_post_data.get('tipo')

            client.save()

            messages.info(request, 'Usuário criado com sucesso')

            return redirect(constants.ROUTE['clients'])
    else:
        form = ClientsForm()

        return render(request, f'{constants.CRUD_PATH["clients"]}/{constants.FORMS["add"]}',
                      {'form': form, 'tipos': Clients.TIPO})

@login_required
def vehicle(request):
    if request.method == 'POST':

        pass

        #mutable_post_data = request.POST.copy()
        #form = VehicleForm(mutable_post_data)
        #form = ClientsForm(mutable_post_data)

        #clients = form.save(commit=False)
        #clients.veiculos =



    else:

        mutable_post_data = request.POST.copy()
        form = ClientsForm(mutable_post_data)


        form = VehicleForm
        brands = Brand.objects.all().order_by('-created_at')

        modelo = request.GET.get('modelo_filter')
        ano = request.GET.get('ano_filter')

        vehicle = Vehicle.objects.all().order_by('-created_at')

        if modelo:
            vehicle = vehicle.filter(modelo__icontains=modelo)
        if ano:
            vehicle = vehicle.filter(ano__icontains=ano)

        paginator = Paginator(vehicle, 4)
        page = request.GET.get('page')

        vehicle = paginator.get_page(page)

        return render(request, f'{constants.CRUD_PATH["clients"]}/{constants.FORMS["vehicle"]}',
                      {'vehicle': vehicle, 'form': form, 'brands': brands})