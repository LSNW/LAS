from django import forms
from .models import AVFile, LoaderReq
from .handler import processTimestamps
from django.core.exceptions import ValidationError
from . import handler


class SplitForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        avfile = cleaned_data.get('avfile')
        timestamps = cleaned_data.get('timestamps')

        if not avfile:
            raise ValidationError({'avfile': []})

        fileNameData = avfile.name.split('.')
        fileName = ''.join(fileNameData[:-1])
        extension = fileNameData[-1]

        if not (avfile.content_type == 'audio/wav') and not (extension == 'mp3' and avfile.content_type == 'audio/mpeg'):
            raise ValidationError({'avfile': ['Unsupported filetype',]})

        if timestamps:
            times, titles = handler.processTimestamps(timestamps)

            if (not handler.contained(times, avfile, extension)):
                raise ValidationError({'timestamps': ['Timestamps exceed media length',]})
        
        
        cleaned_data['times'] = times
        cleaned_data['titles'] = titles
        cleaned_data['fileName'] = fileName
        cleaned_data['fileType'] = extension #avfile.content_type[6:]
        return cleaned_data


    class Meta:
        model = AVFile
        fields = '__all__'
        widgets = {
            'avfile': forms.FileInput(
				attrs={
					"type":"file",
                    "id":"file-upload",
					}
				),
            'timestamps': forms.Textarea(
                attrs={
                }
            )
        }

class ConvertForm(forms.ModelForm):
    avfile = forms.FileField()
    outType = forms.ChoiceField(choices=["mp3", "wav"])

class LoaderForm(forms.ModelForm):
    class Meta:
        model = LoaderReq
        fields = '__all__'

