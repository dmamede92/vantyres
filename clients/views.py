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

from .VehicleFormSet import VehicleFormSet
from .forms import ClientsForm
from .forms import ClientsFormEdit
from .forms import VehicleForm
from .models import Clients
from .models import Vehicle
from brands.models import Brand
from django.db import IntegrityError


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
    vehicle_form = VehicleForm(prefix='new_vehicle')

    if request.method == 'POST':
        form = ClientsFormEdit(request.POST, instance=client)
        if 'add_veiculo' in request.POST:
            vehicle_form = VehicleForm(request.POST, prefix='new_vehicle')
            if vehicle_form.is_valid():
                new_vehicle = vehicle_form.save(commit=False)
                new_vehicle.client = client
                new_vehicle.save()
                messages.success(request, 'Veículo adicionado com sucesso!')
                # Renderiza novamente a página de edição com os dados atualizados
                return render(request, f'{constants.CRUD_PATH["clients"]}/{constants.FORMS["edit"]}', {
                    'form': form,
                    'client': client,
                    'vehicle_form': VehicleForm(prefix='new_vehicle'),  # Novo formulário vazio para adicionar outro veículo
                    'brands': Brand.objects.all().order_by('-created_at'),
                    'vehicles': client.veiculos.all()  # Passa os veículos do cliente
                })
        elif form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return redirect('clients')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')

    return render(request, f'{constants.CRUD_PATH["clients"]}/{constants.FORMS["edit"]}', {
        'form': form,
        'client': client,
        'vehicle_form': vehicle_form,
        'brands': Brand.objects.all().order_by('-created_at'),
        'vehicles': client.veiculos.all()  # Passa os veículos do cliente
    })


@login_required
def delete(request, id):
    client = get_object_or_404(Clients, pk=id)
    client.delete()

    messages.info(request, 'Client Deleteado com sucesso')
    return redirect(constants.ROUTE['clients'])

def add_submit_vehicle(request):
    mutable_post_data = request.POST.copy()
    vehicle_form = VehicleForm(request.POST)
    vehicle = vehicle_form.save(commit=False)

    print(vehicle.ano)
    print(vehicle.modelo)

    mutable_post_data['veiculos'] = vehicle

    return mutable_post_data


@login_required
def new(request):
    if request.method == 'POST':
        data_nascimento_str = request.POST.get('data_nascimento')
        data_nascimento_formatada = datetime.strptime(data_nascimento_str, '%d/%m/%Y').strftime('%Y-%m-%d')
        mutable_post_data = request.POST.copy()
        mutable_post_data['data_nascimento'] = data_nascimento_formatada

        client_form = ClientsForm(mutable_post_data)
        vehicle_formset = VehicleFormSet(mutable_post_data, prefix='veiculos')

        if client_form.is_valid():
            if 'add_veiculo' in request.POST:
                if 'veiculos' not in request.session:
                    request.session['veiculos'] = []

                try:
                    vehicle_data = {
                        'modelo': mutable_post_data['veiculos-0-modelo'],
                        'ano': mutable_post_data['veiculos-0-ano'],
                        'brand': mutable_post_data['brand']
                    }
                    request.session['veiculos'].append(vehicle_data)
                    request.session.modified = True
                except KeyError as e:
                    print(f"Missing data: {e}")

                brands = Brand.objects.all().order_by('-created_at')

                client_form.data['data_nascimento'] = datetime.strptime(data_nascimento_formatada, '%Y-%m-%d').strftime('%d/%m/%Y')

                return render(request, f'{constants.CRUD_PATH["clients"]}/{constants.FORMS["add"]}', {
                    'form': client_form,
                    'vehicle_formset': VehicleFormSet(prefix='veiculos'),
                    'tipos': Clients.TIPO,
                    'is_veiculo': False,
                    'brands': brands,
                    'veiculos': request.session['veiculos'],
                })

            elif 'edit_veiculo' in request.POST:
                brands = Brand.objects.all().order_by('-created_at')

                client_form.data['data_nascimento'] = datetime.strptime(data_nascimento_formatada, '%Y-%m-%d').strftime(
                    '%d/%m/%Y')

                index = int(request.POST['edit_veiculo'])
                print(f'indexss: {index}')
                vehicle_to_edit = request.session['veiculos'][index]
                vehicle_form = VehicleForm(initial=vehicle_to_edit, prefix='veiculos')

                return render(request, f'{constants.CRUD_PATH["clients"]}/{constants.FORMS["add"]}', {
                    'form': client_form,
                    'vehicle_formset': VehicleFormSet(prefix='veiculos'),
                    'vehicle_form': vehicle_form,
                    'tipos': Clients.TIPO,
                    'is_veiculo': False,
                    'brands': brands,
                    'veiculos': request.session['veiculos'],
                })

            else:
                try:
                    client = client_form.save(commit=False)
                    veiculos = request.session.get('veiculos', [])

                    client.save()

                    for veiculo_data in veiculos:
                        vehicle_form = VehicleForm({
                            'modelo': veiculo_data['modelo'],
                            'ano': veiculo_data['ano'],
                            'brand': veiculo_data['brand'],
                        }, instance=Vehicle(client=client))
                        if vehicle_form.is_valid():
                            vehicle_form.save()

                    del request.session['veiculos']
                    return redirect(constants.ROUTE['clients'])
                except IntegrityError as e:
                    print("Cai aqui no Integrity")
                    client_form.add_error('email', 'Email já cadastrado.')
                    client_form.data['data_nascimento'] = datetime.strptime(data_nascimento_formatada, '%Y-%m-%d').strftime('%d/%m/%Y')

        else:
            print("Client form is not valid")
            print(client_form.errors)
    else:
        client_form = ClientsForm()
        vehicle_formset = VehicleFormSet(prefix='veiculos')

    brands = Brand.objects.all().order_by('-created_at')
    return render(request, f'{constants.CRUD_PATH["clients"]}/{constants.FORMS["add"]}', {
        'form': client_form,
        'vehicle_formset': vehicle_formset,
        'tipos': Clients.TIPO,
        'is_veiculo': False,
        'brands': brands,
        'veiculos': request.session.get('veiculos', []),
    })
