from django import forms

class Cupon_Aplly_Form(forms.Form):
    code = forms.CharField()