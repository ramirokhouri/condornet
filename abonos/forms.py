from django import forms
from .models import Cliente, Cobrador, Abono, Recaudacion

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CobradorForm(forms.ModelForm):
    class Meta:
        model = Cobrador
        fields = '__all__'

class AbonoForm(forms.ModelForm):
    class Meta:
        model = Abono
        fields = '__all__'

class RecaudacionForm(forms.ModelForm):
    cobrador = forms.ChoiceField(widget=forms.Select())
    class Meta:
        model = Recaudacion
        fields = ['cobrador']
