from django import forms
from .models import test_image_upload

class Test_form(forms.ModelForm):

    class Meta:
        model = test_image_upload
        fields = ['image']