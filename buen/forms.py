#forms.py
from django import forms  
from .models import Genarator  
class EmployeeForm(forms.ModelForm):  
    class Meta:  
        model = Genarator  
        fields = ['stock'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'stock': forms.Select(attrs={ 'class': 'form-control' }), 
            # 'last_name': forms.TextInput(attrs={ 'class': 'form-control' }),
            # 'email': forms.EmailInput(attrs={ 'class': 'form-control' }),
            #  'contact': forms.NumberInput(attrs={ 'class': 'form-control' }),
            # 'serial_number': forms.TextInput(attrs={ 'class': 'form-control' }),
            #  'stock': forms.Select(attrs={ 'class': 'form-control' }),
            # 'date_sold': forms.DateInput(attrs={ 'class': 'form-control hasDatepicker', 'id':'datepickerNoOfMonths', 'placeholder':'MM/DD/YYYY' }),
            #  'time_sold': forms.TimeInput(attrs={ 'class': 'form-control ui-timepicker-input'  }),
      }



