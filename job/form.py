from django import forms
from .models import Apply,Job

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = '__all__'
        exclude = ('job',)

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('owner','slug')        