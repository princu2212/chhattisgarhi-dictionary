from django import forms
from .models import AddWord

class dictionary(forms.ModelForm):
    class Meta:
        model = AddWord
        fields = ['hindi', 'english', 'chhattisgarhi']
        widgets = {
            'hindi' : forms.TextInput(attrs={'class':'form-control'}),
            'english' : forms.TextInput(attrs={'class':'form-control'}),
            'chhattisgarhi' : forms.TextInput(attrs={'class':'form-control'}),
        }
            
        