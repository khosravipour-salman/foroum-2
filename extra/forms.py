from django import forms


class TagSearchForm(forms.Form):
	name = forms.CharField()