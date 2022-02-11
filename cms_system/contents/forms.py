from django import forms
from .models import Contents, Contents_Description, Theme

class ContentsUploadForm(forms.ModelForm):
    class Meta:
        model = Contents
        fields = ['title', 'upload_file']

class ContentsDescriptionForm(forms.ModelForm):
    class Meta:
        model = Contents_Description
        fields = ['description']

class SelectThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['themeValue']

    def __init__(self, *args, **kwargs):
        super(SelectThemeForm, self).__init__(*args, **kwargs)
        self.fields['themeValue'].queryset = Theme.objects.all().values_list('themeValue', flat=True).order_by('id')

