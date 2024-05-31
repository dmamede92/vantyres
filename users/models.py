from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

from profiles.models import Profile


class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome, senha=None):
        if not email:
            raise ValueError('O campo de email é obrigatório')

        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
        )

        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password):
        user = self.create_user(
            email=email,
            nome=nome,
            senha=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    STATUS = (('ati', 'Ativo'), ('ina', 'Inativo'))
    TIPO = (('fis', 'Pessoa Fisica'), ('jud', 'Pessoa Juridica'))

    email = models.EmailField(verbose_name='E-mail', max_length=255, unique=True)
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=8, choices=TIPO)
    cpf_cnpj = models.CharField(max_length=14, blank=False, null=False)
    data_nascimento = models.DateField(null=False, blank=True)
    status = models.CharField(max_length=8, default='ati', choices=STATUS)
    telefone_celular = models.CharField(max_length=12, blank=True, null=True, verbose_name='Telefone Celular:')
    telefone_comercial = models.CharField(max_length=12, blank=True, null=True, verbose_name='Telefone Comercial:')
    cep = models.CharField(max_length=9, blank=True, null=True, verbose_name='CEP:')
    logradouro = models.CharField(max_length=255, blank=True, null=True, verbose_name='Logradouro:')
    complemento = models.CharField(max_length=255, blank=True, null=True, verbose_name='Complemento:')
    numero = models.CharField(max_length=10, blank=True, null=True, verbose_name='Número:')
    cidade = models.CharField(max_length=100, blank=True, null=True, verbose_name='Cidade:')
    estado = models.CharField(max_length=2, blank=True, null=True, verbose_name='Estado:')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    profiles = models.ForeignKey(Profile(), on_delete=models.SET_NULL, null=True, verbose_name='Perfis:')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff
