from django.db import models


class Profile(models.Model):
    objects = None
    STATUS = (
        ('ati', 'Ativo'),
        ('ina', 'Inativo'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=8, default='ati', choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['name']

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return self.is_staff

    def __str__(self):
        return self.name
