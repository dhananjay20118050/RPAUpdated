from django import forms
from RPAPanel.models import Nodes, Hubs
from django.core.exceptions import ValidationError


class NodesForm(forms.ModelForm):
    class Meta:
        model = Nodes
        fields = "__all__"
        # fields = ('name','email','password','roleid')


class HubsForm(forms.ModelForm):
    class Meta:
        model = Hubs
        fields = "__all__"
