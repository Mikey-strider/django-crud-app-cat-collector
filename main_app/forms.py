from django import forms
from .models import Feeding

class FeedingForm(forms.ModelForm):
	# this is like configuration options for the class 
	class Meta:
		model = Feeding
		fields = ['date', 'meal']
		# widgets property allows you to customize, the inputs
		# add new attributes, etc

		# customizing the 'date' input into a datepicker
		widgets = {
			'date': forms.DateInput(
				format=('%y-%m-%d'),
				attrs={
					'placeholder': 'Select a date',
					'type': 'date'
				}
			),
			# 'meal': forms.Select(
			# 	attrs={
			# 		'id': 'jims-id'
			# 	}
			# )
		}