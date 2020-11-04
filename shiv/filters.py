import django_filters
from django_filters import CharFilter

from django import forms

from .models import *

class ProjectFilter(django_filters.FilterSet):
	project_name = CharFilter(field_name='project_name', lookup_expr="icontains", label='Project Name')
	tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(),
		widget=forms.CheckboxSelectMultiple
		)
	class Meta:
		model = Project
		fields = ['project_name', 'tags']