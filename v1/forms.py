from django.forms import ModelForm,Form,widgets,fields
from v1.models import Type,Person

RADIO_CHOICES=(
    ('0',"ON"),
    ('1',"OFF"),
)

class typeadd(ModelForm):


    class Meta:
        model = Type

        fields = "__all__"

class userli(ModelForm):

    class Meta:
        model = Person
        fields = "__all__"