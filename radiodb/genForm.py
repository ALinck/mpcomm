from django.forms import ModelForm
from radiodb.models import MassportMaster

class RadioForm(ModelForm):
    class Meta:
        model = MassportMaster
        fields = ['unit_id',
                  'serial_number',
                  'model',
                  'model_number',
                  'type',
                  'flash',
                  'flashport',
                  'current',
                  'status',
                  'issued_to',
                  'last_prog',
                  'codeplug',
                  'operation',
                  'date',
                  'notes',]

form = RadioForm()

entry = MassportMaster.objects.get(pk=1)