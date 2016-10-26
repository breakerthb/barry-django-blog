from django import forms

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file = forms.FileField()

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()