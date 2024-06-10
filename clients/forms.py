from django import forms
from django.forms import inlineformset_factory

from .models import Clients
from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('modelo', 'ano')


VehicleFormSet = inlineformset_factory(Clients, Vehicle, form=VehicleForm, extra=1, can_delete=True)


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('nome', 'tipo', 'email', 'cpf_cnpj', 'data_nascimento', 'rg', 'telefone_celular',
                  'telefone_comercial', 'cep', 'logradouro', 'complemento', 'numero',
                  'cidade', 'estado')

        widgets = {
            'cep': forms.TextInput(attrs={'id': 'id_cep', 'class': 'cep'}),
            'tipo': forms.TextInput(attrs={'id': 'id_tipo', 'class': 'tipo'}),
            'cpf_cnpj': forms.TextInput(attrs={'id': 'id_cpf_cnpj', 'class': 'cpf_cnpj'}),
            'rg': forms.TextInput(attrs={'id': 'id_rg', 'class': 'rg'}),
            'telefone_celular': forms.TextInput(attrs={'id': 'id_telefone_celular', 'class': 'phone'}),
            'data_nascimento': forms.DateInput(attrs={'id': 'id_data_nascimento', 'class': 'data_nascimento'},
                                               format='%d/%m/%Y'),
            'logradouro': forms.TextInput(attrs={'id': 'id_logradouro'}),
            'complemento': forms.TextInput(attrs={'id': 'id_complemento'}),
            'numero': forms.TextInput(attrs={'id': 'id_numero'}),
            'cidade': forms.TextInput(attrs={'id': 'id_cidade'}),
            'estado': forms.TextInput(attrs={'id': 'id_estado'}),
        }

        labels = {
            'nome': 'Nome:',
            'email': 'Email:',
            'cpf_cnpj': 'CPF/CNPJ:',
            'tipo': 'Tipo de pessoa:',
            'telefone_celular': 'Telefone Celular:',
            'telefone_comercial': 'Telefone Comercial:',
            'cep': 'CEP:',
            'logradouro': 'Logradouro:',
            'complemento': 'Complemento:',
            'numero': 'Número:',
            'cidade': 'Cidade:',
            'estado': 'Estado:',
            'rg': 'RG:',
            'data_nascimento': 'Data de Nascimento:'
        }


class ClientsFormEdit(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('nome', 'tipo', 'email', 'cpf_cnpj', 'data_nascimento', 'rg', 'telefone_celular',
                  'telefone_comercial', 'cep', 'logradouro', 'complemento', 'numero',
                  'cidade', 'estado', 'status')

        widgets = {
            'cep': forms.TextInput(attrs={'id': 'id_cep', 'class': 'cep'}),
            'cpf_cnpj': forms.TextInput(attrs={'id': 'id_cpf_cnpj', 'class': 'cpf_cnpj'}),
            'telefone_celular': forms.TextInput(attrs={'id': 'id_telefone_celular', 'class': 'phone'}),
            'data_nascimento': forms.DateInput(
                attrs={'id': 'id_data_nascimento', 'class': 'data_nascimento', 'readonly': 'true'}, format='%d/%m/%Y'),
            'logradouro': forms.TextInput(attrs={'id': 'id_logradouro'}),
            'complemento': forms.TextInput(attrs={'id': 'id_complemento'}),
            'numero': forms.TextInput(attrs={'id': 'id_numero'}),
            'cidade': forms.TextInput(attrs={'id': 'id_cidade'}),
            'estado': forms.TextInput(attrs={'id': 'id_estado'}),
        }

        labels = {
            'nome': 'Nome:',
            'email': 'Email:',
            'cpf_cnpj': 'CPF/CNPJ:',
            'tipo': 'Tipo de pessoa:',
            'telefone_celular': 'Telefone Celular:',
            'telefone_comercial': 'Telefone Comercial:',
            'cep': 'CEP:',
            'logradouro': 'Logradouro:',
            'complemento': 'Complemento:',
            'numero': 'Número:',
            'cidade': 'Cidade:',
            'estado': 'Estado:',
            'rg': 'RG:',
            'data_nascimento': 'Data de Nascimento:'
        }
