from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50, label='Su nombre por favor: ')
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)
    website = forms.URLField(max_length=1000, initial='http://')
