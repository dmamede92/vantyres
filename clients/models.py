from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from brands.models import Brand


class Vehicle(models.Model):
    objects = None

    modelo = models.CharField(max_length=30)
    ano = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    brands = models.ForeignKey(Brand(), on_delete=models.SET_NULL, null=True, verbose_name='Marcas:')




class Clients(models.Model):
    objects = None
    STATUS = (
        ('ati', 'Ativo'),
        ('ina', 'Inativo'),
    )
    TIPO = (('fis', 'Pessoa Fisica'), ('jud', 'Pessoa Juridica'))

    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=8, choices=TIPO, null=True)
    email = models.EmailField(verbose_name='E-mail', max_length=255, unique=True)
    cpf_cnpj = models.CharField(max_length=14, blank=False, null=False)
    rg = models.CharField(max_length=10, blank=False, null=True)
    data_nascimento = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=8, default='ati', choices=STATUS)
    telefone_celular = models.CharField(max_length=12, blank=True, null=True, verbose_name='Telefone Celular:')
    telefone_comercial = models.CharField(max_length=12, blank=True, null=True, verbose_name='Telefone Comercial:')
    cep = models.CharField(max_length=9, blank=True, null=True, verbose_name='CEP:')
    logradouro = models.CharField(max_length=255, blank=True, null=True, verbose_name='Logradouro:')
    complemento = models.CharField(max_length=255, blank=True, null=True, verbose_name='Complemento:')
    numero = models.CharField(max_length=10, blank=True, null=True, verbose_name='Número:')
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade:')
    estado = models.CharField(max_length=2, blank=True, null=True, verbose_name='Estado:')
    veiculos = models.CharField(max_length=15, blank=True, null=True, verbose_name='Veiculos:')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['nome']

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    def __str__(self):
        return self.nome
