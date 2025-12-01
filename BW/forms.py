from django.forms import ModelForm, Form, ChoiceField, IntegerField, CharField, BooleanField
from BW.models import Bikes

# , bike_types

# import , TextField,

class FilterForm(Form):
    bike_type = ChoiceField(choices=Bikes.bike_types, required=False)


class BikeInformationForm(Form):
    bike_type = IntegerField(choices=Bikes.bike_types, default=4)
    name = CharField(max_length=25)
    description = CharField(max_length=1024)
    price = IntegerField(default=None)
    is_there_any = BooleanField(default=False)
    bike_amount = IntegerField()



