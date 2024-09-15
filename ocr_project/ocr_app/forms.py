# ocr_project/ocr_app/forms.py

from django import forms

class UploadImageForm(forms.Form):
    image = forms.ImageField(required=False)
    text = forms.CharField(widget=forms.Textarea, required=False)
    language = forms.ChoiceField(choices=[
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('it', 'Italian'),
        ('pt', 'Portuguese'),
        ('nl', 'Dutch'),
        ('ru', 'Russian'),
        ('ja', 'Japanese'),
        ('zh', 'Chinese'),
        ('ar', 'Arabic'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
        ('pa', 'Punjabi'),
        ('sw', 'Swahili'),
        ('zu', 'Zulu'),
        ('xh', 'Xhosa'),
        ('tn', 'Tswana'),
        ('ss', 'Siswati'),
        ('lu', 'Lunda'),
        ('ny', 'Chewa'),
        ('bem', 'Bemba'),
        ('ton', 'Tonga'),
        ('nya', 'Nyanja'),
        ('en-ZM', 'English (Zambia)'),
        ('tn-ZM', 'Tswana (Zambia)'),
        ('zu-ZM', 'Zulu (Zambia)'),
        ('xh-ZM', 'Xhosa (Zambia)'),
        ('ss-ZM', 'Siswati (Zambia)'),
        ('bem-ZM', 'Bemba (Zambia)'),
        ('ton-ZM', 'Tonga (Zambia)'),
        ('nya-ZM', 'Nyanja (Zambia)'),
        # Add more languages as needed
    ])
