from django.forms import ModelForm,Form,widgets,fields,ModelMultipleChoiceField,forms,CheckboxSelectMultiple
from v1.models import Type,Person,Plan

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

class plangroup(ModelForm):

    list = ModelMultipleChoiceField(widget=CheckboxSelectMultiple,queryset=Type.objects.all())
    class Meta:
        model = Plan
        fields = "__all__"
