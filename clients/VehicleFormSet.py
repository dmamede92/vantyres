from django.forms import inlineformset_factory

from clients.forms import VehicleForm
from clients.models import Clients, Vehicle

VehicleFormSet = inlineformset_factory(Clients, Vehicle, form=VehicleForm, extra=1, can_delete=True)
