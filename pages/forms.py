from django import forms

class Content(forms.Form):
    text = forms.CharField(max_length=1000, label='Please Enter Text to Analyze (1000 character limit)', widget=forms.Textarea(attrs={'class':'form-control', 'rows': '4'}))
    