from django import forms
from .models import Feeding


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