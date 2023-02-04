from django import forms

class NewGraph(forms.Form):
    graph_name = forms.CharField(label='Producer Abreviation', max_length=100)