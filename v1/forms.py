from django.forms import ModelForm
from v1.models import Type,Person

class typeadd(ModelForm):

    class Meta:
        model = Type

        fields = "__all__"

class userli(ModelForm):

    class Meta:
        model = Person
        fields = "__all__"