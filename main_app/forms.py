from django import forms
from .models import Feeding

<<<<<<< HEAD
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
=======

class FeedingForm(forms.ModelForm):

    # config options that your class needs to do what it needs to do
    # this needs certain info to do what needs to happen
    class Meta:
        model = Feeding
        fields = ("date", "meal")  # widgets property allows you to customize the inputs
        # customizing the date input
        widgets = {
            "date": forms.DateInput(
                format=("%y-%m-%d"),
                attrs={"placeholder": "Select a date", "type": "date"},
            )
        }
>>>>>>> 9b4e396adaec23043e4f1f29ffbb455999e9633b
