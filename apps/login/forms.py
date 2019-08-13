# -*- coding: utf-8 -*-
from django import forms

class DocumentForm(forms.Form):
    profile_pic = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )