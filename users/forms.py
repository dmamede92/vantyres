from django import forms
from django.contrib.auth.forms import AuthenticationForm

from profiles.models import Profile
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'profiles', 'password', 'tipo',
                  'telefone_celular', 'telefone_comercial', 'cep', 'logradouro',
                  'complemento', 'numero', 'cidade', 'estado', 'cpf_cnpj', 'data_nascimento')

        widgets = {
            'password': forms.PasswordInput(),
            'cep': forms.TextInput(attrs={'id': 'id_cep', 'class': 'cep'}),
            'tipo': forms.TextInput(attrs={'id': 'id_tipo', 'class': 'tipo'}),
            'cpf_cnpj': forms.TextInput(attrs={'id': 'id_cpf_cnpj', 'class': 'cpf_cnpj'}),
            'telefone_celular': forms.TextInput(attrs={'id': 'id_telefone_celular', 'class': 'phone'}),
            'data_nascimento': forms.DateInput(attrs={'id': 'id_data_nascimento', 'class': 'data_nascimento'}, format='%d/%m/%Y'),
            'logradouro': forms.TextInput(attrs={'id': 'id_logradouro'}),
            'complemento': forms.TextInput(attrs={'id': 'id_complemento'}),
            'numero': forms.TextInput(attrs={'id': 'id_numero'}),
            'cidade': forms.TextInput(attrs={'id': 'id_cidade'}),
            'estado': forms.TextInput(attrs={'id': 'id_estado'}),
        }

        labels = {
            'password': 'Senha',
            'cpf_cnpj': 'CPF/CNPJ',
            'tipo': 'Tipo de pessoa',
            'telefone_celular': 'Telefone Celular',
            'telefone_comercial': 'Telefone Comercial',
            'cep': 'CEP',
            'logradouro': 'Logradouro',
            'complemento': 'Complemento',
            'numero': 'Número',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'data_nascimento': 'Data de Nascimento'
        }


class UsuarioFormEdit(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'status', 'tipo', 'telefone_celular',
                  'telefone_comercial', 'cep', 'logradouro', 'complemento',
                  'numero', 'cidade', 'estado', 'cpf_cnpj', 'data_nascimento')

        widgets = {
            'cep': forms.TextInput(attrs={'id': 'id_cep', 'class': 'cep'}),
            'cpf_cnpj': forms.TextInput(attrs={'id': 'id_cpf_cnpj', 'class': 'cpf_cnpj'}),
            'telefone_celular': forms.TextInput(attrs={'id': 'id_telefone_celular', 'class': 'phone'}),
            'data_nascimento': forms.DateInput(attrs={'id': 'id_data_nascimento', 'class': 'data_nascimento', 'readonly': 'true'}, format='%d/%m/%Y'),
            'logradouro': forms.TextInput(attrs={'id': 'id_logradouro'}),
            'complemento': forms.TextInput(attrs={'id': 'id_complemento'}),
            'numero': forms.TextInput(attrs={'id': 'id_numero'}),
            'cidade': forms.TextInput(attrs={'id': 'id_cidade'}),
            'estado': forms.TextInput(attrs={'id': 'id_estado'}),
        }

        labels = {
            'cpf_cnpj': 'CPF/CNPJ:',
            'data_nascimento': 'Data de Nascimento:',
            'nome': 'Nome:',
            'tipo': 'Tipo:',
            'status': 'Status:'
        }

    profiles = forms.ModelChoiceField(queryset=Profile.objects.all(),
                                      empty_label="Selecione o perfil")

    def __init__(self, *args, **kwargs):
        super(UsuarioFormEdit, self).__init__(*args, **kwargs)
        if self.instance.profiles:
            self.fields['profiles'].initial = self.instance.profiles
            self.fields['profiles'].label = 'Perfis:'


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = Usuario
        fields = ['email', 'senha']
