from django import forms

class Content(forms.Form):
    text = forms.CharField(label='Please Paste Text', widget=forms.Textarea(attrs={'class':'form-control', 'rows': '2'}))
    