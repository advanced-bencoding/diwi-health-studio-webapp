from django import forms
from django.forms import ModelForm
from appointment.models import Appointment

#Form for appointment editing
class EditAppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('date', 'time_start', 'time_end')

        labels = {
            'date': '',
            'time_start': '',
            'time_end': '',
        }

        widgets = {
            'date': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'date'}),
            'time_start': forms.TimeInput(attrs={'class':'form-control', 'placeholder': 'Start Time'}),
            'time_end': forms.TimeInput(attrs={'class':'form-control', 'placeholder': 'End Time'}),
        }
        